# Final_Project

<br>

The project codelabs instructions: https://codelabs-preview.appspot.com/?file_id=https://docs.google.com/document/d/11HC-1LpisJTqCnSOU2hKEpsWQpU3qmPzW1dlcs4RZ8o#0
<br>

Shakespearify - AI Animator

<br>
Overview
Welcome to Shakespearify, an innovative project that combines the power of AI-driven storytelling and illustration to modernize Shakespeare's plays for today's audience. Our goal is to bridge the gap between classic literature and modern technology, reimagining Shakespeare's timeless stories for a digital-savvy audience while revitalizing interest in his works.
  <br>
    <br>
The demo video: https://drive.google.com/drive/folders/1iChOHqXDGNkagqMBW2yNeglPAgA79wfX?usp=share_link
   <br>
   <br>
About Shakespearify  <br>
Shakespearify is an exciting project that leverages cutting-edge technologies to transform Shakespearean plays into visually appealing and easily digestible content. Here's what we've accomplished:  <br>
Segmentation and extraction of Shakespearean texts using AI tools.  <br>
Generation of artistic prompts with OpenAI's API for vibrant illustrations.  <br>
Hosting of narratives on Streamlit for an interactive experience.  <br>
Secure data management on Google Cloud Platform.  <br>
Technologies and Tools  <br>
Architecture  <br>
Proposed Architecture:
  <br>
![proposedARCHITEC_project](https://github.com/BigDataIA-Fall2023-Team5/Final_Project/blob/main/MicrosoftTeams-image%20(9).png)

  <br>
Executed Architecture:
  <br>
 ![ARCHITEC_project](https://github.com/BigDataIA-Fall2023-Team5/Final_Project/blob/main/MicrosoftTeams-image%20(10).png)

  <br>
Frontend UI  <br>
FastAPI: An intuitive framework for rapid development and deployment of web services.  <br>
Streamlit: A cutting-edge application framework for creating data-driven applications.  <br>
Data Sourcing  <br>
1. "Beautiful Stories from Shakespeare" <br>
Source: Project Gutenberg <br>
Nature: A digital library offering public domain literary works. <br>
Accessibility: Freely accessible online. <br>
Advantages: Simplified and abridged versions of Shakespeare's works for easy AI processing. <br>
2. User-Provided EPUB Files <br>
Source: User uploads.  <br>
Nature: EPUB files for a wide range of literature.  <br>
Advantages: Enables personalized comics and a broader range of source material.  <br>
Data Processing  <br>
Apache Airflow: Three distinct pipelines for data scraping, EPUB processing, and prompt generation/image creation.  <br>
Data Staging  <br>
Google Firestore: Flexible and scalable database for managing segmented texts of plays.  <br>
MongoDB Atlas: Open-source NoSQL database for storing images and prompts.  <br>
AWS S3 Bucket: Scalable object storage service for storing images.  <br>
Data Processing  <br>
OpenAI API for Prompt Generation: Advanced natural language processing for generating creative prompts.  <br>
Stable Diffusion API for Image Generation: State-of-the-art image generation tool for creating captivating illustrations.  <br>
Running the code:  <br>
Access the application via your web browser at http://localhost:8000  <br>
The FastAPI link is https://fastapi-comicstrip-9d8ed8b29b40.herokuapp.com/docs#/default/segment_chapter_segment_chapter__post  <br>
User Guide  <br>
Landing Page: Start on the landing page to explore illustrated plays.  <br>
EPUB Upload: Upload your own EPUB files to create personalized comics.  <br>
Dynamic Animation: Customize art styles, CFG scale, seed, and steps to create unique comic strips.  <br>
Project Workflow  <br>
Data Scraping and Segmentation: Extracting data from various sources and segmenting it for storytelling.  <br>
EPUB Processing: Handling user-uploaded EPUB files for content extraction.  <br>
Prompt Generation and Image Creation: Creating engaging prompts and generating images.  <br>
Data Storage: Data storage on Google Firestore, MongoDB Atlas, and AWS S3.  <br>
Contributors
   <br>
WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR ASSIGNMENT AND ABIDE BY THE
  <br>

Anamika Bharali : 33.3%  <br>
Saniya Kapur : 33.3%  <br>
Shruti Mundargi : 33.3%  <br>
License  <br>
This project is licensed under the MIT License - see the LICENSE file for details.  <br>
Acknowledgments  <br>
We would like to express our gratitude to Prof. Sri Krishnamurthy for his guidance and support throughout this project.  <br>