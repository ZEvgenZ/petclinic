pipeline {
   /*  agent {
        //указываем, что выполнять задачу хотим внутри 
        // Docker-контейнера на базе указанного образа:
        docker {
            image 'docker'
        }
    }
    */

    stages {
        stage('Pull from Git') {
            steps {
                checkout scm
            }
        }
        
        stage('Package') {
            steps {
                sh 'Docker build .'
                }
        }
        
    }
}
/* 
//ad5a78f7-c1af-4b37-a58f-ae20d9244457
// grebec/petclinic:latest
#_ Этап сборки нового Docker-образа и его загрузки с систему Artifactory:
node {
    stage('Create im') {
     def customImage = docker.build("my-image:${env.BUILD_ID}")
            customImage.push()}
 }
docker.withRegistry('https://registry.example.com')
            
        docker.withRegistry("https://repo.artifactory.bank", "LoginToArtifactory") {
            def dkrImg = docker.build("repo.artifactory.bank/dev-backend:${env.BUILD_ID}")
            dkrImg.push()
            dkrImg.push('latest')
        }
	}
    stage('Заливаем его в Artifactory') {
        docker.withRegistry("https://repo.artifactory.bank", "LoginToArtifactory") {
            sh "docker service update --image repo.artifactory.bank/dev-backend:${env.BUILD_ID} SMB_dev-backend"
        }
    }
}
*/
