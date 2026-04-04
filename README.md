# ACEest Fitness App – CI/CD Pipeline Assignment

## Project Overview

This project implements a complete **DevOps CI/CD pipeline** for the ACEest Fitness & Gym application.

The original application was built using **Tkinter (desktop-based UI)** and has been successfully migrated into a **Flask web application** to enable automation, scalability, and CI/CD integration.



## Objectives

* Convert Tkinter app → Flask web app
* Implement Version Control using GitHub
* Add Unit Testing using Pytest
* Containerize application using Docker
* Automate CI/CD using GitHub Actions
* Implement Jenkins build pipeline



## Tech Stack

* Python (Flask)
* SQLite Database
* Pytest
* Docker
* GitHub Actions
* Jenkins



## Application Features

* User Login System (Admin)
* Client Management
* AI-based Program Generation
* Workout Tracking
* Membership Tracking
* PDF Report Generation
* Progress Chart Visualization



## Local Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/SK907797/Fitness-App.git
cd fitness-app
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Application

```bash
python app.py
```

### 5. Access Application

Open browser:

```
http://127.0.0.1:5000
```

### Default Login

```
Username: admin
Password: admin
```



## Running Tests

```bash
pytest
```



## Docker Usage

### Build Image

```bash
docker build -t aceest-app .
```

### Run Container

```bash
docker run -p 5000:5000 aceest-app
```



## CI/CD Pipeline (GitHub Actions)

The pipeline is triggered on every:

* push
* pull_request

### Steps:

1. Checkout code
2. Setup Python
3. Install dependencies
4. Run tests (pytest)
5. Build Docker image



## Jenkins Integration

Jenkins is used as a **build automation tool**.

### Functionality:

* Executes build pipeline
* Runs tests
* Validates application

### Note:

Due to plugin/network constraints, Jenkins was configured using a simplified build approach, ensuring successful build execution.



## CI/CD Workflow

```
GitHub Push → GitHub Actions → Test → Docker Build → Jenkins Build
```



## Key Learning Outcomes

* CI/CD pipeline implementation
* Docker containerization
* Flask web development
* DevOps workflow automation
* Debugging real-world issues (Jenkins plugins, environment setup)



## Conclusion

This project demonstrates a complete DevOps lifecycle implementation from development to automated deployment, ensuring reliability, scalability, and continuous integration.



## Author

Shantha Kumar U
