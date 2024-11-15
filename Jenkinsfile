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
        stage('Imprimir PATH') {
            steps {
                bat 'echo %PATH%'
            }
        }
        stage('Verificar Python') {
            steps {
                bat 'python --version'
            }
        }
        stage('Instalar dependencias') {
            steps {
                script {
                    dir("${params.PROJECT}") {
                        if (params.PROJECT == 'USQL') {
                            bat('python -m pip install ply')
                        } else if (params.PROJECT == 'TRIVIA') {
                            bat('python -m pip install pandas')
                        }
                    }
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    dir("${params.PROJECT}") {
                        echo "Construyendo el proyecto ${params.PROJECT}..."
                        if (params.PROJECT == 'USQL') {
                            bat('python tests.py')
                        } else if (params.PROJECT == 'PEDIDOS') {
                            bat('javac -Xlint:unchecked Main.java')
                            bat('java Main')
                        } else if (params.PROJECT == 'TRIVIA') {
                            bat('python main.py')
                        }
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    dir("${params.PROJECT}") {
                        echo "Desplegando el proyecto ${params.PROJECT}..."
                    }
                }
            }
        }
    }
}
