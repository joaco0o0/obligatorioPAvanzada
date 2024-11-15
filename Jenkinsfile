pipeline {
    agent any
    parameters {
        choice(name: 'PROJECT', choices: ['USQL', 'PEDIDOS', 'TRIVIA'], description: 'Seleccione el proyecto a ejecutar')
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/joaco0o0/obligatorioPAvanzada.git', branch: 'main'
            }
        }

        stage('Instalar dependencias') {
            steps {
                script {
                    if (params.PROJECT == 'TRIVIA' || params.PROJECT == 'USQL') {
                        bat ('python -m pip install pandas')
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo "Directorio actual: ${pwd()}"

                    if (params.PROJECT == 'USQL') {
                        echo "Ejecutando tests para USQL..."
                        bat('python USQL\\tests.py')
                    } 
                    else if (params.PROJECT == 'PEDIDOS') {
                        echo "Compilando y ejecutando PEDIDOS..."

                        bat """
                            javac -source 8 -target 8 -Xlint:unchecked -d PEDIDOS\\out ^
                            PEDIDOS\\src\\main\\java\\org\\example\\Main.java ^
                            PEDIDOS\\src\\main\\java\\org\\example\\Pedido\\Pedido.java ^
                            PEDIDOS\\src\\main\\java\\org\\example\\Processing\\Tarea.java ^
                            PEDIDOS\\src\\main\\java\\org\\example\\Processing\\ProcesadorPedidos.java ^
                            PEDIDOS\\src\\main\\java\\org\\example\\Processing\\ProcesamientoPago.java ^
                            PEDIDOS\\src\\main\\java\\org\\example\\Processing\\EmpaquetadoPedidos.java ^
                            PEDIDOS\\src\\main\\java\\org\\example\\Processing\\Envio.java

                        """

                        bat('java -cp PEDIDOS\\out org.example.Main')
                    }
                    else if (params.PROJECT == 'TRIVIA') {
                        echo "Ejecutando TRIVIA..."
                        bat('python TRIVIA\\main.py')
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
                body: """El pipeline de ${params.PROJECT} ha finalizado correctamente. :) """
            )
            emailext(
                to: 'mariogcarminatti@gmail.com',
                subject: "Pipeline completado: ${params.PROJECT}",
                body: """<p>El pipeline de ${params.PROJECT} ha finalizado correctamente. :) """
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
