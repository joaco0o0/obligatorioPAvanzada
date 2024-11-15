pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    def projects = ['PEDIDOS', 'USQL', 'TRIVIA']
                    for (project in projects) {
                        dir(project) {
                            echo "Checking out $project"
                            checkout([
                                $class: 'GitSCM',
                                branches: [[name: '*/joaco']],
                                userRemoteConfigs: [[
                                    url: "https://github.com/joaco0o0/obligatorioPAvanzada.git",
                                ]]
                            ])
                        }
                    }
                }
            }
        }
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
