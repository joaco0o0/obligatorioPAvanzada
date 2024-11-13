pipeline {
    agent any

    environment {
        TRIVIA_DIR = 'TRIVIA'
        PEDIDOS_DIR = 'PEDIDOS'
        USQL_DIR = 'USQL'
    }

    stages {
        
    

        

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
