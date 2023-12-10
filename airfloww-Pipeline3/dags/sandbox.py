import os
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models.param import Param
from datetime import timedelta
import os
import openai
from openai import OpenAI
import requests
import base64
import re
from pymongo import MongoClient

user_input = {
    "datasource_url1": Param(default="https://www.sec.gov/files/form1.pdf", type='string', minLength=5, maxLength=255),
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

def prompt_engineering(**kwargs):
    openai.api_key = os.getenv("OPENAI_KEY")

    comic_prompts = []

    client = OpenAI()

    def get_questions(text):

            response = client.chat.completions.create(
            model="gpt-4",
            messages=[
            {
            "role": "system",
            "content": """this text is a story, how to chunk this text like this when you want to use those chunks to form prompts for image generation to form a comic strip out of the whole text. Give me image prompts in such a way that I can create a sensible comic strip out of those image prompts. Give 8 chunks in format: \n 1. Image prompt: "Text example"
    2. Image prompt: "Text example"
    3. Image prompt: "Text example"\n"""
            },
            {
            "role": "user",
            "content": f"\"\"\"\n{text}\n\"\"\""
            }
            ],
            temperature=1,
            max_tokens=800,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )

            first_choice = response.choices[0]
            message_content = first_choice.message.content

            print("==========")
            print(message_content)

            return message_content


    for part in enumerate(parts):
        comic_prompts.append(get_questions(part))
    
    separated_prompts = [prompt.strip() for text in comic_prompts for prompt in re.split(r'\n\d+\. Image prompt: ', text) if prompt]


    return separated_prompts

def api_call(prompt, image_number):

    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

    body = {
        "steps": 40,
        "width": 1024,
        "height": 1024,
        "seed": 0,
        "cfg_scale": 5,
        "samples": 1,
        "style_preset": "fantasy-art",
        "text_prompts": [
        {
            "text": f"{prompt}",
            "weight": 1
        },
        {
            "text": "blurry, bad",
            "weight": -1
        }
        ],
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": os.getenv("SD_KEY"),
    }

    response = requests.post(
        url,
        headers=headers,
        json=body,
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    # make sure the out directory exists
    if not os.path.exists("./out"):
        os.makedirs("./out")

    for i, image in enumerate(data["artifacts"]):
        with open(f'./out/image_{image_number}_{i}.png', "wb") as f:
            f.write(base64.b64decode(image["base64"]))


def stable_diffusion(**kwargs):
    separated_prompts = prompt_engineering(**kwargs)
    image_number = 1

    for prompt in separated_prompts:
        print(image_number)
        api_call(prompt, image_number)
        image_number += 1

def store_images_and_prompts(**kwargs):
    image_folder_path = './out'
    separated_prompts = prompt_engineering(**kwargs)
    client = MongoClient('mongodb_connection_string')  # Replace with your MongoDB connection string
    db = client['your_database']  # Replace with your database name
    collection = db['your_collection']  # Replace with your collection name

    def is_valid_image(filename):
        parts = filename.split('_')
        if len(parts) == 3 and parts[0] == 'image' and parts[2].endswith('.png'):
            try:
                int(parts[1])  # Check if the middle part is an integer
                return True
            except ValueError:
                return False
        return False

    image_files = sorted(
        filter(is_valid_image, os.listdir(image_folder_path)),
        key=lambda x: int(x.split('_')[1])
    )

    num_iterations = min(len(image_files), len(separated_prompts))

    for i in range(num_iterations):
        image_file = image_files[i]
        text = separated_prompts[i]
        image_path = os.path.join(image_folder_path, image_file)

        with open(image_path, 'rb') as file:
            encoded_image = file.read()

        document = {
            'image_name': image_file,
            'prompt': text,
            'image_data': encoded_image  # Storing the binary data of the image
        }
        collection.insert_one(document)





with dag:
    prompt_engineering_task = PythonOperator(
        task_id="prompt_engineering",
        python_callable=prompt_engineering,
        dag=dag,
    )

    stable_diffusion_task = PythonOperator(
        task_id='stable_diffusion',
        python_callable=stable_diffusion,
        dag=dag,
    )

    store_images_and_prompts_task = PythonOperator(
        task_id='store_images_and_prompts',
        python_callable=store_images_and_prompts,
        dag=dag,
    )

    bye_world_task = BashOperator(
        task_id="bye_world",
        bash_command='echo "Bye from airflow"'
    )

    prompt_engineering_task >> stable_diffusion_task >> store_images_and_prompts_task >> bye_world_task