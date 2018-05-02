pipeline {
    agent any
    tools { 
        maven 'Maven 3.5' 
    }
    stages {
    stage ('Build') {
            steps {
                checkout scm
                echo 'This is a minimal pipeline.'
                sh 'mvn package'
            }
        }
    }
}
