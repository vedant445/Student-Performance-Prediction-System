# 🎓 Student Performance Prediction System

A complete **Machine Learning Operations (MLOps)** project that predicts whether a student will **Pass** or **Fail** based on academic, family, and lifestyle attributes.

The project demonstrates an end-to-end ML workflow including data preprocessing, model training, evaluation, deployment using **Streamlit**, containerization with **Docker**, orchestration using **Kubernetes**, and monitoring using **Prometheus** and **Grafana**.

---

## 🚀 Features

- 📊 Student Performance Prediction
- 🧹 Data Preprocessing Pipeline
- 🤖 Machine Learning Model Training
- 📈 Model Evaluation
- 🎯 Real-time Prediction
- 🌐 Streamlit Web Application
- 🐳 Docker Containerization
- ☸ Kubernetes Deployment
- 📡 Prometheus Monitoring
- 📊 Grafana Dashboard
- 🔄 GitHub Version Control

---

## 🛠 Tech Stack

### Programming Language
- Python 3.12

### Machine Learning
- Scikit-Learn
- Pandas
- NumPy
- Joblib

### Web Framework
- Streamlit

### DevOps & MLOps
- Docker
- Docker Compose
- Kubernetes
- Prometheus
- Grafana

### Cloud & Version Control
- Git
- GitHub
- Streamlit Community Cloud

---

## 📂 Project Structure

```
Student-MLOps/
│
├── app/
│   ├── app.py
│   ├── style.py
│   ├── Prediction.py
│   ├── Analytics.py
│   └── About.py
│
├── data/
│
├── models/
│   ├── model.pkl
│   └── scaler.pkl
│
├── src/
│   ├── data_ingestion.py
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│   └── utils.py
│
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
│
├── monitoring/
│   ├── docker-compose.yml
│   └── prometheus.yml
│
├── Dockerfile
├── requirements.txt
├── README.md
└── mlflow.db
```

---

## ⚙️ Machine Learning Pipeline

```
Dataset
    │
    ▼
Data Ingestion
    │
    ▼
Data Preprocessing
    │
    ▼
Feature Engineering
    │
    ▼
Model Training
    │
    ▼
Model Evaluation
    │
    ▼
Model Serialization (.pkl)
    │
    ▼
Streamlit Application
```

---

## 🐳 Docker

Build Docker Image

```bash
docker build -t student-mlops .
```

Run Container

```bash
docker run -p 8501:8501 student-mlops
```

---

## ☸ Kubernetes Deployment

Deploy application

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

Check deployment

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

---

## 📡 Monitoring with Prometheus

Prometheus continuously collects metrics from the Streamlit application.

Example metrics include:

- Application Visits
- CPU Usage
- Memory Usage
- Python Runtime Metrics

Prometheus endpoint

```
http://localhost:9090
```

---

## 📊 Grafana Dashboard

Grafana visualizes metrics collected by Prometheus.

Dashboard can display:

- Application Visits
- CPU Usage
- Memory Usage
- Response Time
- System Metrics

Grafana URL

```
http://localhost:3000
```

Default Credentials

```
Username: admin
Password: admin
```

---

## 🌐 Streamlit Application

Run locally

```bash
streamlit run app/app.py
```

Application URL

```
http://localhost:8501
```

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/vedant445/Student-Performance-Prediction-System.git
```

Move into project directory

```bash
cd Student-Performance-Prediction-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app/app.py
```

---

## 📈 Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | **88.61%** |
| Precision | **95.83%** |
| Recall | **86.79%** |
| F1 Score | **91.09%** |

---

## 📷 Project Workflow

```
                 User
                   │
                   ▼
          Streamlit Application
                   │
                   ▼
        Machine Learning Model
                   │
         Prediction (Pass/Fail)
                   │
     ┌─────────────┴─────────────┐
     │                           │
     ▼                           ▼
Docker Container         Prometheus Metrics
     │                           │
     └─────────────┬─────────────┘
                   ▼
               Grafana Dashboard
                   │
                   ▼
             Kubernetes Cluster
```

---

## 🎯 Future Improvements

- CI/CD using GitHub Actions
- MLflow Model Registry
- AWS Deployment
- Database Integration
- User Authentication
- Model Retraining Pipeline
- Automated Monitoring Alerts

---

## 👨‍💻 Author

**Vedant Maladkar**

GitHub: https://github.com/vedant445

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
