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
pipeline {
    agent any
    parameters {
        choice(name: 'PROJECT', choices: ['USQL', 'PEDIDOS', 'TRIVIA'], description: 'Seleccione el proyecto a ejecutar')
    }
    stages {

    
        stage('Instalar dependencias') {
                steps {
                    script {
                        dir ("obligatorioPAvanzada/${params.PROJECT}"){
                            if (params.PROJECT == 'USQL') {
                                sh('python3 -m pip install ply')

                            } 
                            
                            else if (params.PROJECT == 'TRIVIA') {
                                sh('python3 -m pip install pandas')
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
                            sh ('python3 Test.py')
                        } 
                        else if (params.PROJECT == 'PEDIDOS') {
                            sh('javac -Xlint:unchecked Main.java')
                            sh('java Main')
                        }

                        else if (params.PROJECT == 'TRIVIA') {
                            sh ('python3 main.py')
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

