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
                        bat('python C:\\Users\\jhere\\OneDrive\\Documentos\\GitHub\\obligatorioPAvanzada\\USQL\\tests.py')
                    } 
                    else if (params.PROJECT == 'PEDIDOS') {
                        echo "Compilando y ejecutando PEDIDOS..."
                        bat('javac -Xlint:unchecked C:\\Users\\jhere\\OneDrive\\Documentos\\GitHub\\obligatorioPAvanzada\\PEDIDOS\\src\\main\\java\\org\\example\\Main.java')
                        bat('java -cp C:\\Users\\jhere\\OneDrive\\Documentos\\GitHub\\obligatorioPAvanzada\\PEDIDOS\\src\\main\\java org.example.Main')
                    }
                    else if (params.PROJECT == 'TRIVIA') {
                        echo "Ejecutando TRIVIA..."
                        bat('python C:\\Users\\jhere\\OneDrive\\Documentos\\GitHub\\obligatorioPAvanzada\\TRIVIA\\main.py')
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo "Desplegando el proyecto ${params.PROJECT}..."
                // Aquí puedes agregar los pasos específicos de despliegue si es necesario
            }
        }
    }

    post {
        success {
            emailext(
                to: 'jherede@gmail.com',
                subject: "Pipeline completado: ${params.PROJECT}",
                body: """<p>El pipeline de <b>${params.PROJECT}</b> ha finalizado correctamente.</p>"""
            )
        }
        failure {
            emailext(
                to: 'jherede@gmail.com',
                subject: "Pipeline fallido: ${params.PROJECT}",
                body: """<p>El pipeline de <b>${params.PROJECT}</b> ha fallado.</p>"""
            )
        }
    }
}
