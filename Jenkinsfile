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
                git clone https://github.com/yourusername/flask-app.git
                cd flask-app
                '''
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                #!/bin/sh
                python3 -m venv ${VENV_DIR}  # Create virtual environment
                . ${VENV_DIR}/bin/activate  # Activate virtual environment
                pip install flask  # Install Flask
                '''
            }
        }

        stage('Run Flask Application') {
            steps {
                sh '''
                #!/bin/sh
                . ${VENV_DIR}/bin/activate
                python app.py &
                '''
            }
        }
    }
}
