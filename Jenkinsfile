pipeline {
    agent any
    stages {
        
        stage('Build') {
            steps {
                echo 'Cloning repository'
                git branch: 'master', url: 'https://github.com/raul-rodsa/test'
                
                echo 'Installing dependencies'
                sh 'pip3 install -r requirements.txt'
                
            }
        }
        
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        
        stage('Packet'){
            steps {
               sh 'docker build . -t rauleitor97/test-1'
            }
        }
        
        stage('Test image'){
            steps{
                echo 'Analizing with trivy'
                sh 'trivy i --severity HIGH,CRITICAL --ignore-unfixed rauleitor97/test-1'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}