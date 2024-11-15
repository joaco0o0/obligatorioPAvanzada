pipeline {
    agent any
    parameters {
        choice(name: 'PROJECT', choices: ['USQL', 'PEDIDOS', 'TRIVIA'], description: 'Seleccione el proyecto a ejecutar')
    }

    environment {
        JAVA_HOME = "C:/Program Files/Java/jdk-21"
        PATH = "${JAVA_HOME}/bin;${env.PATH}"
    }
    stages {
        stage('Instalar dependencias') {
            steps {
                script {
                    dir ("obligatorioPAvanzada/${params.PROJECT}") {
                        if (params.PROJECT == 'USQL') {
                            bat('python3 -m pip install ply')
                        } 
                        else if (params.PROJECT == 'TRIVIA') {
                            bat('python3 -m pip install pandas')
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
                            bat('python3 Test.py')
                        } 
                        else if (params.PROJECT == 'PEDIDOS') {
                            bat('javac -Xlint:unchecked Main.java')
                            bat('java Main')
                        }
                        else if (params.PROJECT == 'TRIVIA') {
                            bat('python3 main.py')
                        }
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    dir("obligatorioPAvanzada/${params.PROJECT}") {
                        echo "Desplegando el proyecto ${params.PROJECT}..."
                    }
                }
            }
        }
    }
}
