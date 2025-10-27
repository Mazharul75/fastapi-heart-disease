🫀 Heart Disease Prediction API

Mod 10: FastAPI + Docker + Deployment Project

🚀 Live Demo

🔗 Swagger UI: https://fastapi-heart-disease.onrender.com/docs#/

Use this link to explore and test the API endpoints interactively.

📘 Project Overview

This project is a FastAPI-based machine learning web service for predicting heart disease.
It is trained on the Heart Disease Dataset from Kaggle and deployed using Docker and Render.

The primary goal of this assignment is to:

Build a simple ML model for prediction

Create a FastAPI REST API

Dockerize the application

Deploy it to Render

🧠 Features

GET /health → Health check endpoint

GET /info → Displays model information and feature list

POST /predict → Accepts patient data and predicts heart disease presence

🧩 Tech Stack
Component	Technology
Backend Framework	FastAPI
Machine Learning	Scikit-learn
Model Storage	Joblib
Containerization	Docker, Docker Compose
Deployment Platform	Render
Language	Python 3.10+
📂 Project Structure
fastapi_heart_disease/
│
├── app/
│   ├── main.py              # FastAPI main application
│   ├── schemas.py           # Pydantic models for request validation
│
├── model/
│   ├── model_run.py         # Model training script
│   ├── heart_model.joblib   # Saved ML model
│
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker image configuration
├── docker-compose.yml       # Local Docker setup
└── README.md                # Project documentation

🧰 Setup Instructions (Local)
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/fastapi-heart-disease.git
cd fastapi-heart-disease

2️⃣ Train the Model (Optional)

Run the model script if you want to retrain:

python model/model_run.py

3️⃣ Run Locally with Docker
docker-compose up --build


Access the API at 👉 http://localhost:8000/docs

⚙️ Deployment on Render

Steps followed for deployment:

Pushed project to GitHub

Created a Render Web Service

Selected Docker environment

Connected GitHub repo

Waited for build and deployment

Live API available here:
🔗 https://fastapi-heart-disease.onrender.com/docs#/

🧪 Example API Request
Endpoint: /predict

Method: POST

Sample Input:

{
  "age": 45,
  "sex": 1,
  "cp": 2,
  "trestbps": 130,
  "chol": 230,
  "fbs": 0,
  "restecg": 1,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 3,
  "ca": 0,
  "thal": 2
}


Sample Output:

{
  "heart_disease": false
}

🧑‍💻 Author

Name: Mazharul Islam
Course: Ostad — Module 10 Project
Instructor: [Your Instructor’s Name]
Deployment URL: https://fastapi-heart-disease.onrender.com/docs#/