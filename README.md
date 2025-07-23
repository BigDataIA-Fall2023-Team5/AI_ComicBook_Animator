
# Shakespearify - AI Animator

Welcome to **Shakespearify**, an innovative project that combines AI-driven storytelling and illustration to modernize Shakespeare's plays for today’s digital audience.

Our goal is to bridge the gap between classic literature and modern technology—reimagining Shakespeare's timeless stories while revitalizing interest in his works.

---

##  Project Instructions  
 [Click here to access Codelabs Instructions](https://codelabs-preview.appspot.com/?file_id=https://docs.google.com/document/d/11HC-1LpisJTqCnSOU2hKEpsWQpU3qmPzW1dlcs4RZ8o#0)

 [Watch the Demo Video](https://drive.google.com/drive/folders/1iChOHqXDGNkagqMBW2yNeglPAgA79wfX?usp=share_link)

---

## Project Overview

**Shakespearify** leverages cutting-edge technologies to transform Shakespearean plays into visually appealing and easily digestible content.

Key Features:
- AI-powered segmentation and extraction of Shakespearean texts  
- Prompt generation with OpenAI API for vibrant illustrations  
- Hosting of narratives on Streamlit for interactivity  
- Secure data management using Google Cloud Platform  

---

## 🛠️ Technologies and Tools

### Architecture

**Proposed Architecture:**  
![Proposed Architecture](https://github.com/BigDataIA-Fall2023-Team5/Final_Project/blob/main/arch0.png)

**Executed Architecture:**  
![Executed Architecture](https://github.com/BigDataIA-Fall2023-Team5/Final_Project/blob/main/arch1.png)

---

### Frontend UI
- **FastAPI**: For building web services  
- **Streamlit**: For data-driven app interface  

---

### 📚 Data Sourcing

**1. Beautiful Stories from Shakespeare**  
- Source: Project Gutenberg  
- Nature: Public domain digital library  
- Advantage: Simplified versions suitable for AI processing  

**2. User-Provided EPUB Files**  
- Source: User uploads  
- Nature: Versatile literature inputs  
- Advantage: Enables personalized comic generation  

---

## 🔄 Data Processing

- **Apache Airflow**: Orchestrates three pipelines:
  - Data scraping
  - EPUB processing
  - Prompt/image generation  

---

## 🗃️ Data Staging

- **Google Firestore**: Segmented texts storage  
- **MongoDB Atlas**: Stores images and prompts  
- **AWS S3**: Scalable object storage for image assets  

---

## 🧠 AI & Image Generation

- **OpenAI API**: For creative prompt generation  
- **Stable Diffusion API**: For image rendering from prompts  

---

## 🚀 Running the Code

- Open the application in your browser at:  
  `http://localhost:8000`

- FastAPI interactive docs:  
  [FastAPI Swagger UI](https://fastapi-comicstrip-9d8ed8b29b40.herokuapp.com/docs#/default/segment_chapter_segment_chapter__post)

---

## 📖 User Guide

- **Landing Page**: Explore curated illustrated Shakespeare plays  
- **EPUB Upload**: Create comics from your own books  
- **Animation Control**: Customize:
  - Art styles  
  - CFG scale  
  - Seed  
  - Number of inference steps  

---

## 🔁 Project Workflow

1. **Data Scraping & Segmentation**  
2. **EPUB Processing**  
3. **Prompt Generation & Image Creation**  
4. **Data Storage** in Firestore, MongoDB Atlas, and S3  

---

## 👥 Contributors

> We attest that we haven’t used any other students’ work in our assignment and abide by the academic integrity policy.

- **Anamika Bharali** – 33.3%  
- **Saniya Kapur** – 33.3%  
- **Shruti Mundargi** – 33.3%  

---

## 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

## 🙏 Acknowledgments

Special thanks to **Prof. Sri Krishnamurthy** for his guidance and support throughout this project.
