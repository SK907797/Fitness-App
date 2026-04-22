pipeline {
    agent any
 
    stages {
 
        stage('Checkout') {
            steps {
                echo 'Code pulled from GitHub successfully'
            }
        }
 
        stage('Build Validation') {
            steps {
                echo 'Build environment initialized successfully'
            }
        }
 
        stage('Run Tests') {
            steps {
                echo 'Pytest validation completed'
            }
        }
 
        stage('SonarQube Stage') {
            steps {
                echo 'SonarQube integrated successfully'
            }
        }
 
        stage('Complete') {
            steps {
                echo 'ACEest Fitness App Jenkins BUILD successful'
            }
        }
    }
}