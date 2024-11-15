pipeline {
    agent any

    stages {
        stage('Build PEDIDOS') {
            steps {
                script {
                    echo "Construyendo el proyecto PEDIDOS"
                    dir('PEDIDOS') {
                        sh './gradlew build'
                    }
                }
            }
        }

        stage('Test TRIVIA') {
            steps {
                script {
                    echo "Ejecutando pruebas para TRIVIA"
                    dir('TRIVIA') {
                        sh 'python3 -m unittest tests.py'
                    }
                }
            }
        }

        stage('Test USQL') {
            steps {
                script {
                    echo "Ejecutando pruebas para USQL"
                    dir('USQL') {
                        sh 'python3 -m unittest tests.py'
                    }
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    echo "Limpiando archivos temporales"
                    sh 'find . -name "*.pyc" -exec rm -f {} +'
                    sh './gradlew clean'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completado.'
            cleanWs()
        }
        success {
            echo 'Build exitosa.'
        }
        failure {
            echo 'Build fallida.'
        }
    }
}
