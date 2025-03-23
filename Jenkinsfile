pipeline {
    agent any

    environment {
        PYTHONPATH = "C:\\Users\\myaka\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages"
        PYTHON_EXE = "C:\\Users\\myaka\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
    }

    stages {
        stage('Example') {
            steps {
                script {
                    bat "echo Hello World"
                }
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Upgrade pip and install dependencies
                    bat "\"%PYTHON_EXE%\" -m pip install --upgrade pip"
                    bat "\"%PYTHON_EXE%\" -m pip install --force-reinstall markupsafe"
                    bat "\"%PYTHON_EXE%\" -m pip install -r requirements.txt"
                }
            }
        }

        stage('Run Script') {
            steps {
                script {
                    bat "\"%PYTHON_EXE%\" reg.py"
                }
            }
        }
    }
}
