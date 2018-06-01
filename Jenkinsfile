pipeline {
        agent none 
    stages {
        stage('Get from GIT') {
                agent {
      
        docker {
            image 'maven'
        }
    }
            steps {
                checkout scm
            }
        }
        stage('Build') {
                 agent {
   
        docker {
            image 'maven'
        }
    }
            steps {
               sh 'mvn package'
              // archiveArtifacts 'target/*.jar'
            }
 
        }
     
       stage('LS') {
                      agent {
       
        docker {
            image 'maven'
        }
    }
            steps {
                sh 'cd /var/lib/jenkins/workspace/petclinic/target/ && ls -la'
               
                }
         }         
   
   stage('LSWORK') {
                  agent any
            steps { 
                sh 'cd /var/lib/jenkins/workspace/petclinic/target/ && ls -la'
         }
   
            stage('docker_build') {
                  agent any
            steps { 
                sh 'docker build . test:test'
         }
            }           
   }
   }
}     
/*
#_ Этап сборки нового Docker-образа и его загрузки с систему Artifactory:
node {
    stage('Собираем образ') {
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
      /* stage('Copy Archive') {
         steps {
             script {
                 step ([$class: 'CopyArtifact',
                        projectName: 'petclinic',
                        filter: "target/*.jar",
                   target: '/home/ubuntu/app']);
             }
        
        }
    }
   */
