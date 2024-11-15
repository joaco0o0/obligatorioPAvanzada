pipeline {
    agent any

    environment {
        JAVA_HOME = "C:/Program Files/Java/jdk-21" 
        PATH = "${JAVA_HOME}/bin;${env.PATH}"
    }
    stages {
        

        stage('Instalar dependencias') {
                steps {
                    script {
                        dir ("PA_Final/${params.PROJECT}"){
                            if (params.PROJECT == 'UDSL') {
                                sh('python3 -m pip install ply')

                            } 
                            
                            else if (params.PROJECT == 'Trivia') {
                                sh('python3 -m pip install pandas')
                            }
                        }
                    }
                }

        }   
    }
}