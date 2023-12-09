import os
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models.param import Param
from datetime import timedelta
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import math

user_input = {
    "epub_path": Param(default="/opt/airflow/dags/carroll-alice-in-wonderland-illustrations.epub", type='string', minLength=5, maxLength=255),
    "chapter_title": Param(default="I Down the Rabbit-hole", type='string', minLength=5, maxLength=255),
}


dag = DAG(
    dag_id="sandbox",
    schedule="0 0 * * *",   
    start_date=days_ago(0),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=["labs", "damg7245"],
    params=user_input,
)

def file_reader(**kwargs):
    epub_path = kwargs["params"]["epub_path"]
    book = epub.read_epub(epub_path)
    index_headings = ['contents', 'chapters', 'index']  # Common index page headings
    chapter_titles = []

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.content, 'html.parser')
            # Check if this document is an index page
            if any(heading in soup.text.lower() for heading in index_headings):
                # Extract potential chapter titles
                links = soup.find_all('a')
                for link in links:
                    chapter_title = link.get_text().strip()
                    if chapter_title:
                        chapter_titles.append(chapter_title)
                break  # Assuming only one index page
    print(chapter_titles)


    chapter_title = kwargs["params"]["chapter_title"]
    chapters_content = {}
    # Iterate through each item in the EPUB file
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(item.get_content(), 'html.parser')
        # Find all the header tags that might indicate a chapter start
        for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            title = header.get_text(strip=True)
            if title:
                chapters_content[title] = soup.get_text()

    # Now chapters_content has all chapters' text indexed by their title
    return chapters_content



def segmentation(**kwargs):
  parts_dict = {}
  original_dict = file_reader(**kwargs)
  for key, value in original_dict.items():
    sentences = sent_tokenize(value)

    # Determining the length of each part
    total_sentences = len(sentences)
    part_length = math.ceil(total_sentences / 4)

    # Dividing the sentences into four parts
    parts = [sentences[i:i + part_length] for i in range(0, total_sentences, part_length)]
    
    
    parts_dict[key] = parts

    return parts_dict

with dag:
    file_reader_task = PythonOperator(
        task_id="file_reader",
        python_callable=file_reader,
        dag=dag,
    )

    segmentation_task = PythonOperator(
        task_id='segmentation',
        python_callable=segmentation,
        dag=dag,
    )

    bye_world_task = BashOperator(
        task_id="bye_world",
        bash_command='echo "Bye from airflow"'
    )

    file_reader_task >> segmentation_task >> bye_world_task
