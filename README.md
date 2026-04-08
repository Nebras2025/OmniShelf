# OmniShelf 📚

**A Full-Stack Book Recommendation System**

OmniShelf is a **data-driven full-stack web application** that provides personalized book recommendations using **Machine Learning**. It combines a robust backend, clean UI, efficient database handling, and modern cloud deployment practices.

The recommendation engine uses a **K-Nearest Neighbors (KNN)** model trained on curated book-rating data to suggest books based on user interests.

---

## ✨ Features

* **Smart Recommendations:** Uses a **KNN model** to suggest similar books.
* **Data-Driven:** Powered by book titles, authors, user ratings, and metadata.
* **Modern Backend:** Built with **Flask + SQLAlchemy**.
* **Interactive UI:** Clean and user-friendly frontend for searching books.
* **Containerized:** Fully **Dockerized** for reproducible environments.
* **CI/CD Ready:** Automated deployment using **GitHub Actions**.
* **Cloud Native:** Deployable on **AWS ECS Fargate + ECR**.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Web Framework:** Flask
* **Database:** SQLAlchemy (SQLite)
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **DevOps:** Docker, GitHub Actions
* **Cloud:** AWS ECS, ECR, CloudWatch
* **Deployment:** ECS Fargate

---

## 📦 Installation & Local Setup

### 1) Clone the repository

```bash
git clone https://github.com/Nebras2025/OmniShelf.git
cd OmniShelf
```

### 2) Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run the Flask app

```bash
python app.py
```

The application will run on:

```bash
http://localhost:5000
```

---

## 🐳 Docker Setup

Build Docker image:

```bash
docker build -t omnishelf-app .
```

Run container:

```bash
docker run -p 5000:5000 omnishelf-app
```

---

## ☁️ AWS ECS Deployment

OmniShelf is production-ready for **AWS ECS Fargate deployment**.

### CI/CD Flow

1. Push code to `main`
2. GitHub Actions builds Docker image
3. Pushes image to **Amazon ECR**
4. Updates **ECS task definition**
5. Deploys to **ECS Fargate service**

---

## 🤖 ML Recommendation Engine

The recommendation engine uses:

* **K-Nearest Neighbors (KNN)**
* cosine similarity
* user-book interaction matrix
* feature preprocessing with Pandas/NumPy

This allows the app to recommend books similar to a selected title.

---

## 🚀 Future Improvements

* User authentication
* PostgreSQL migration
* Redis caching
* Personalized user history
* Hybrid recommender system
* MLOps model versioning

---

## 👨‍💻 Author

Built by **Nebras** as a portfolio-grade **Data Science + MLOps + Full Stack project**.

This project demonstrates:

* ML engineering
* backend development
* Docker
* CI/CD
* cloud deployment
* production-grade app architecture
