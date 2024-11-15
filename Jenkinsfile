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
                        dir ("obligatorioPAvanzada/${params.PROJECT}"){
                            if (params.PROJECT == 'USQL') {
                                sh('python3 -m pip install ply')

                            } 
                            
                            else if (params.PROJECT == 'TRIVIA') {
                                sh('python3 -m pip install pandas')
                            }
                        }
                    }
                }

        }
        stage('Build') {
            steps {
                script {
                    dir("obligatorioPAvanzada/${params.PROJECT}") {

                        echo "Construyendo el proyecto ${params.PROJECT}..."
                        if (params.PROJECT == 'USQL') {
                            sh ('python3 Test.py')
                        } 
                        else if (params.PROJECT == 'PEDIDOS') {
                            sh('javac -Xlint:unchecked Main.java')
                            sh('java Main')
                        }

                        else if (params.PROJECT == 'TRIVIA') {
                            sh ('python3 main.py')
                        }
                    }
                    
                }
            }
        }
   
    }
}