pipeline {
    agent any

    environment {
        JAVA_HOME = "C:/Program Files/Java/jdk-21" 
        PATH = "${JAVA_HOME}/bin;${env.PATH}"
    }

    stages {
        stage('Build') {
            steps {
                script {
                    echo "Construyendo el proyecto PEDIDOS con Gradle en Windows"
                    dir('PEDIDOS') {
                        bat 'gradlew.bat clean build'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "Ejecutando pruebas unitarias para PEDIDOS"
                    dir('PEDIDOS') {
                        bat 'gradlew.bat test --info'
                    }
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                script {
                    echo "Publicando resultados de pruebas"
                    junit 'PEDIDOS/build/test-results/test/*.xml'
                }
            }
        }

        stage('Archive Artifacts') {
            steps {
                script {
                    echo "Archivando archivos JAR generados"
                    archiveArtifacts artifacts: 'PEDIDOS/build/libs/*.jar', allowEmptyArchive: true
                }
            }
        }
    }

    post {
        always {
            echo 'Limpieza del entorno de trabajo'
            cleanWs()
        }
        success {
            echo 'Pipeline completado exitosamente.'
        }
        failure {
            echo 'Pipeline fallido. Revisa los errores.'
        }
    }
}
