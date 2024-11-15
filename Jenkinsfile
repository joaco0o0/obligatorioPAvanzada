pipeline {
    agent any
    parameters {
        choice(name: 'PROJECT', choices: ['USQL', 'PEDIDOS', 'TRIVIA'], description: 'Seleccione el proyecto a ejecutar')
    }
    environment {
        PYTHON_ENV = 'C:\\Python310'
        JAVA_HOME = 'C:\\Program Files\\Java\\jdk-11.0.12'
    }
    stages {
        stage('Validación de parámetros') {
            steps {
                script {
                    if (!['USQL', 'PEDIDOS', 'TRIVIA'].contains(params.PROJECT)) {
                        error "Proyecto no válido seleccionado: ${params.PROJECT}"
                    }
                }
            }
        }

        stage('Checkout') {
            steps {
                git url: 'https://github.com/joaco0o0/obligatorioPAvanzada.git', branch: 'main'
            }
        }

        stage('Instalar dependencias') {
            steps {
                script {
                    if (params.PROJECT == 'TRIVIA' || params.PROJECT == 'USQL') {
                        bat("${PYTHON_ENV}\\python.exe -m pip install -r requirements.txt || exit 0")
                    }
                }
            }
        }

        stage('Compilación y Ejecución') {
            steps {
                script {
                    if (params.PROJECT == 'USQL') {
                        echo "Ejecutando tests para USQL..."
                        bat("${PYTHON_ENV}\\python.exe USQL\\tests.py")
                    } 
                    else if (params.PROJECT == 'PEDIDOS') {
                        echo "Compilando PEDIDOS con javac..."
                        bat("""
                            ${JAVA_HOME}\\bin\\javac -source 8 -target 8 -Xlint:unchecked -d PEDIDOS\\out ^
                            PEDIDOS\\src\\main\\java\\org\\example\\Main.java ^
                            PEDIDOS\\src\\main\\java\\org\\example\\Pedido\\Pedido.java ^
                            PEDIDOS\\src\\main\\java\\org\\example\\Processing\\*.java
                        """)
                        bat("${JAVA_HOME}\\bin\\java -cp PEDIDOS\\out org.example.Main")
                    } 
                    else if (params.PROJECT == 'TRIVIA') {
                        echo "Ejecutando TRIVIA..."
                        bat("${PYTHON_ENV}\\python.exe TRIVIA\\main.py")
                    }
                }
            }
        }

        stage('Pruebas') {
            steps {
                script {
                    echo "Ejecutando pruebas para ${params.PROJECT}..."
                    if (params.PROJECT == 'PEDIDOS') {
                        bat("${JAVA_HOME}\\bin\\java -cp PEDIDOS\\out org.example.Test")
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo "Desplegando el proyecto ${params.PROJECT}..."
            }
        }
    }

    post {
        success {
            emailext(
                to: 'jherede@gmail.com',
                subject: "Pipeline completado: ${params.PROJECT}",
                body: """<p>El pipeline de <b>${params.PROJECT}</b> ha finalizado correctamente. :) </p>"""
            )
        }
        failure {
            emailext(
                to: 'jherede@gmail.com',
                subject: "Pipeline fallido: ${params.PROJECT}",
                body: """<p>El pipeline de <b>${params.PROJECT}</b> falló. :( </p>"""
            )
        }
    }
}
