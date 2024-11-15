pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    def projects = ['PEDIDOS', 'USQL', 'TRIVIA']
                    for (project in projects) {
                        dir(project) {
                            echo "Building $project"
                            bat "mvn clean package"
                        }
                    }
                }
            }
        }
    }
}

