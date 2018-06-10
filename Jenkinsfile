pipeline {
        agent none 
    stages {
            stage ('list & instances up') {
            agent any

            steps { 
                withCredentials([[
            $class: 'AmazonWebServicesCredentialsBinding',
            credentialsId: '321',
            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
        ]]) {
            sh ('> hosts ')
            sh 'AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} AWS_DEFAULT_REGION=us-east-2 python3 ./start.py' 
            }
            //sleep 150 // seconds
            }
        }
        //######################################################
        //   stage ('create inst') { agent any
        //       steps {
        //         withCredentials([[
        //     $class: 'AmazonWebServicesCredentialsBinding',
        //     credentialsId: '321',
        //     accessKeyVariable: 'AWS_ACCESS_KEY_ID',
        //     secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
        // ]]) 
        //               {
        //     sh ('> hosts ')            
        //     sh ('AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} AWS_DEFAULT_REGION=us-east-2')
        //     //sh ('AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} AWS_DEFAULT_REGION=us-west-2 ${AWS_BIN}')
	    // //sh('/home/ubuntu/print.sh')
        //                 withAWS(region:'us-east-2'){
        //                         sh('python3.5 start.py')} 
        //                 //echo 'Waiting deployment to complete start inst'
        //                 //sleep 200 // seconds
		// 	}
        //        }
        //    }
            stage('Checkout and build') {agent { docker {image 'maven'}}
            steps {
                checkout scm
                sh 'mvn package'
               }
            }
       
            stage('docker_build') {agent any
            steps { 
                sh 'docker build -t zevgenz/petclinic:${BUILD_NUMBER} .'
                sh 'docker images'
                sh 'docker tag zevgenz/petclinic:${BUILD_NUMBER} zevgenz/petclinic:latest'    
                withDockerRegistry([ credentialsId: "ID_DockerHub", url: ""]) 
                { sh 'docker push zevgenz/petclinic:latest'}
            }
            }          
            //     stage ('Start_APP') { agent any       
            //  steps {      
            //     ansiblePlaybook(
            //     playbook: 'app.yml',
            //     inventory: 'hosts',
            //     installation: 'Ans1',
            //     credentialsId: 'AWS_ssh_key',
            //     disableHostKeyChecking: true) }
            // } 

            stage ('use ansible') {
            
            agent any

            steps {
                withCredentials(bindings: [sshUserPrivateKey(credentialsId: 'AWS_ssh_key',
                                                             keyFileVariable: 'SSH_KEY_FOR_ABC')]) {
                  //create database
                  sh "ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ./hosts --private-key=${SSH_KEY_FOR_ABC}  ./app.yml"
                }

            }
        }
   }
}     

