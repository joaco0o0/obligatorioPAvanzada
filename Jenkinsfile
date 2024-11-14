pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    def projects = ['Pedidos', 'USQL', 'TRIVIA']
                    for (project in projects) {
                        dir(project) {
                            echo "Building $project"
                            sh "mvn clean package"
                        }
                    }
                }
            }
        }
    }
}

