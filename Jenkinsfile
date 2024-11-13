pipeline {
    agent any

    environment {
        TRIVIA_DIR = 'TRIVIA'
        PEDIDOS_DIR = 'PEDIDOS'
        USQL_DIR = 'USQL'
    }

    stages {
        
        stage('Construir Pedidos') {
            steps {
                dir("${PEDIDOS_DIR}") {
                    echo 'Construyendo módulo Pedidos...'
                    sh 'mvn clean install -DskipTests'
                }
            }
        }
        

        stage('saludar') {
            steps {
                echo 'Hola, mundo!'
            }
        }
    }

    post {
        always {
            echo 'Enviando notificación...'
            
        }
    }
}
