# ACEest Fitness & Gym – Advanced DevOps CI/CD Project
## Project Overview
 
ACEest Fitness & Gym is a Flask-based web application developed to demonstrate a complete DevOps lifecycle. This project showcases modern DevOps practices including version control, automated testing, containerization, CI/CD pipelines, code quality analysis, multiple deployment strategies, and cloud deployment.
 
## Objectives
* Develop a functional Flask-based gym management system
* Implement version control using Git & GitHub
* Automate testing using Pytest
* Containerize the application using Docker
* Build CI/CD pipelines using GitHub Actions and Jenkins
* Perform static code analysis using SonarQube
* Implement multiple deployment strategies
* Deploy application on Kubernetes
* Deploy application on cloud platform
 
## Tech Stack
| Category |    Tools |
|----------|--------|
| Backend   | Python, Flask|
| Testing   | Pytest|
| Version Control   | Git, GitHub|
| CI/CD | GitHub Actions, Jenkins|
| Containerization  | Docker|
| Code Quality  | SonarQube|
| Orchestration | Kubernetes|
| Cloud Platform    | Render|
| Registry  | Docker Hub|
 
## Project Structure
fitness-app/
│── app.py
│── requirements.txt
│── Dockerfile
│── Jenkinsfile
│── sonar-project.properties
│── test_app.py
│
├── legacy_versions/
├── k8s/
│   ├── rolling/
│   ├── blue-green/
│   ├── canary/
│   ├── shadow/
│   ├── ab-testing/
│
└── .github/workflows/main.yml
 
## Local Setup
git clone https://github.com/SK907797/Fitness-App
cd aceest-fitness-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

### Access:
http://127.0.0.1:5000
Default Login:
 
Username: admin
Password: admin

### Running Tests
pytest -v test_app.py
### Docker Usage
#### Build image:
docker build -t fitness-app .
#### Run container:
docker run -p 5000:5000 fitness-app
#### Docker Hub Images
shantha087/fitness-app:v1.0
shantha087/fitness-app:v2.0
shantha087/fitness-app:v3.0
shantha087/fitness-app:v3.2.4
shantha087/fitness-app:latest
```
## CI/CD Pipeline
### GitHub Actions
 
Triggered on every push:
 
* Checkout Code
* Install Dependencies
* Run Pytest
* Build Docker Image
 
### Jenkins
 
Used for build validation:
 
* Source Checkout
* Build Validation
* Test Stage
* SonarQube Stage
* Build Completion
 
### SonarQube Integration
* Static code analysis performed
* Identifies bugs, vulnerabilities, code smells
* Ensures maintainability
### Kubernetes Deployment
 
#### Deploy application:
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```
#### Check:
kubectl get pods
kubectl get svc
## Deployment Strategies Implemented
### 1. Rolling Update
kubectl set image deployment/aceest-app aceest-app=prabakaran2311/aceest-app:latest
**Zero downtime upgrade**
 
### 2. Blue-Green Deployment
* Two environments: Blue (current), Green (new)
* Traffic switched via service selector
 
**Instant rollback capability**
 
### 3. Canary Deployment
* Stable + Canary deployments
* Traffic split using replica distribution
 
**Gradual rollout**
 
### 4. A/B Testing ✅
#### Application-Level:
* Flask randomly serves two UI versions
#### Kubernetes-Level:
* Separate deployments for Version A & B
 
**User experience comparison**
 
### 5. Shadow Deployment ✅
* New version deployed but not exposed
* Used for testing without impacting users
 
**Safe validation**
 
## Cloud Deployment
 
Application deployed using container image on cloud platform:
 
* Platform: Render
* Deployment Method: Docker Image
* Public URL available
 
 
## Architecture Flow
```text
Developer → GitHub → GitHub Actions → Docker Hub → Cloud (Render)
                                     → Kubernetes (Local)
                                     → Jenkins (Build Validation)
                                     → SonarQube (Code Quality)
```
## Key Learning Outcomes
* End-to-end CI/CD pipeline implementation
* Docker containerization and versioning
* Jenkins pipeline integration
* SonarQube static analysis
* Kubernetes orchestration
* Rolling updates and deployment strategies
* Cloud deployment fundamentals
* Real-world DevOps workflow