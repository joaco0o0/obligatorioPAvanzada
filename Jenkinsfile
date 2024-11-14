pipeline {
    agent any

    environment {
        TRIVIA_DIR = 'TRIVIA'
        PEDIDOS_DIR = 'PEDIDOS'
        USQL_DIR = 'USQL'
        GITHUB_REPO = 'https://github.com/joaco0o0/obligatorioPAvanzada.git'
        GITHUB_BRANCH = 'main'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    try {
                        echo 'Checking out GitHub repository...'
                        checkout([
                            $class: 'GitSCM',
                            branches: [[name: "*/${GITHUB_BRANCH}"]],
                            userRemoteConfigs: [[
                                url: "${GITHUB_REPO}",
                                credentialsId: 'github-credentials'
                            ]]
                        ])
                    } catch (Exception e) {
                        error "GitHub checkout failed: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Git Config') {
            steps {
                script {
                    try {
                        bat 'git config --global core.autocrlf true'
                        bat 'git config --global --list'
                    } catch (Exception e) {
                        echo "Warning: Git configuration failed: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Compilar') {
            steps {
                script {
                    try {
                        echo 'Compilando...'
                        bat 'mvn clean install -DskipTests'
                    } catch (Exception e) {
                        error "Error en compilación: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Construir Trivia') {
            steps {
                script {
                    try {
                        dir("${TRIVIA_DIR}") {
                            echo 'Construyendo módulo Trivia...'
                            bat 'mvn clean package -DskipTests'
                        }
                    } catch (Exception e) {
                        error "Error en construcción de Trivia: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Construir Pedidos') {
            steps {
                script {
                    try {
                        dir("${PEDIDOS_DIR}") {
                            echo 'Construyendo módulo Pedidos...'
                            bat 'mvn clean package -DskipTests'
                        }
                    } catch (Exception e) {
                        error "Error en construcción de Pedidos: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Construir USQL') {
            steps {
                script {
                    try {
                        dir("${USQL_DIR}") {
                            echo 'Construyendo módulo USQL...'
                            bat 'mvn clean package -DskipTests'
                        }
                    } catch (Exception e) {
                        error "Error en construcción de USQL: ${e.getMessage()}"
                    }
                }
            }
        }
    }
}