//mail bcc: '', body: 'Test', cc: '', from: '', replyTo: '', subject: 'hey', to: 'arjun.cse1313@gmail.com'
pipeline {
    agent any

    stages {
        stage('Example') {
            steps {
                script {
                    // Using double quotes for the outer string
                    bat "echo Hello World"
                    //bat "whoami"
                }
            }
        }
        stage('Run'){
            steps{
                script{
                    //bat "python reg.py" 
                    bat "C:\Users\AL\AppData\Local\Programs\Python\Python312\python.exe python --version"
                    //bat "python --version"
                }
            }
            
        }
    }
}
