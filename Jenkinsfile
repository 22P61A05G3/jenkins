pipeline {
    agent any

    environment {
        VENV_DIR = "/venv" // Virtual environment directory
        SHELL = "/bin/sh" // Use default macOS shell
    }

    stages {
        stage('Clone Repository') {
            steps {
                sh '''
                #!/bin/sh
                rm -rf flask-app
                git clone https://github.com/drsaab1313/web-crud.git
                cd web-crud
                '''
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                #!/bin/sh
                python3 -m venv venv  # Create virtual environment
                . venv/bin/activate  # Activate virtual environment
                pip install flask  # Install Flask
                '''
            }
        }

        stage('Run Flask Application') {
            steps {
                sh '''
                #!/bin/sh
                . venv/bin/activate
                python app.py &
                '''
            }
        }
    }
}
