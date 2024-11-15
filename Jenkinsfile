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
                echo "Current directory: ${pwd()}"

                switch(params.PROJECT) {
                    case 'USQL':
                        echo "Running USQL tests..."
                        bat "python .\\USQL\\tests.py"
                        break

                    case 'PEDIDOS':
                        echo "Building and running PEDIDOS..."
                        def srcFiles = [
                            'Main',
                            'Pedido/Pedido',
                            'Processing/Tarea',
                            'Processing/ProcesadorPedidos',
                            'Processing/ProcesamientoPago',
                            'Processing/EmpaquetadoPedidos',
                            'Processing/Envio'
                        ].collect { ".\\PEDIDOS\\src\\main\\java\\org\\example\\${it}.java" }.join(' ^\n        ')

                        bat """
                            javac -source 8 -target 8 -Xlint:unchecked -d .\\PEDIDOS\\out ^
                            ${srcFiles}
                        """
                        bat "java -cp .\\PEDIDOS\\out org.example.Main"
                        break

                    case 'TRIVIA':
                        echo "Running TRIVIA..."
                        bat ".\\TRIVIA\\main.py"
                        break

                    default:
                        error "Unknown project: ${params.PROJECT}"
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