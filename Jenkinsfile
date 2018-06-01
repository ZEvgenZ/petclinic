pipeline {
    agent {
        //указываем, что выполнять задачу хотим внутри 
        // Docker-контейнера на базе указанного образа:
        docker {
            image 'maven'
        }
    }
    
    stages {
        stage('Стягиваем код из ГИТа') {
            steps {
                checkout scm
            }
        }
        stage('Собираем') {
            steps {
               sh 'mvn package'
            }
 
        }
        
        }
    }
}
