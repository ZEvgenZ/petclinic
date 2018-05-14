pipeline {
        agent {label "worker1"}
    tools { 
        maven 'Maven 3.5' 
    }
    /* environment {
    AWS_BIN = '/home/ec2-user/.local/bin/aws'
    }*/
    stages {
        /*stage ('Build') {
            steps {
                checkout scm
                echo 'This is a minimal pipeline.'
                sh 'mvn package'
            }
        }*/
        stage ('create inst') {
              steps {
                withCredentials([[
            $class: 'AmazonWebServicesCredentialsBinding',
            credentialsId: 'ada1da8c-6363-4223-9c2f-93684d18989a',
            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
        ]]) {
            sh ('AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} AWS_DEFAULT_REGION=us-west-2')
            //sh ('AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} AWS_DEFAULT_REGION=us-west-2 ${AWS_BIN}')
	    //sh('/home/ubuntu/print.sh')
                        withAWS(region:'us-west-2'){
                                sh('python3 start.py')} 
			}
                   
          
        }
    }
           /* stage ('Build') { 
                    steps { 
                             sh ('echo hello') }
            } */
    }
}

       
       
