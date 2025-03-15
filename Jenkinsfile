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
                    bat '"C:\\Users\\myaka\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" reg.py'
                }
            }         
        }
    }
}
