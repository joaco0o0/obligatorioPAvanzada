pipeline {
    agent any

    stages {
        stage('Build PEDIDOS') {
            steps {
                script {
                    echo "Construyendo el proyecto PEDIDOS en Windows"
                    dir('PEDIDOS') {
                        bat 'gradlew.bat build'
                    }
                }
            }
        }

        stage('Test TRIVIA') {
            steps {
                script {
                    echo "Ejecutando pruebas para TRIVIA"
                    dir('TRIVIA') {
                        bat 'python -m unittest tests.py'
                    }
                }
            }
        }

        stage('Test USQL') {
            steps {
                script {
                    echo "Ejecutando pruebas para USQL"
                    dir('USQL') {
                        bat 'python -m unittest tests.py'
                    }
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    echo "Limpiando archivos temporales en Windows"
                    bat 'del /s /q *.pyc'
                    bat 'gradlew.bat clean'
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
