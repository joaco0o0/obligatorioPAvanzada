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
                        dir ("PA_Final/${params.PROJECT}"){
                            if (params.PROJECT == 'TRIVIA') {
                                bat ('python -m pip install pandas')

                            } 
                        }
                    }
                }
        }

        stage('Build') {
            steps {
                script {
                    echo "Directorio actual: ${pwd()}"

                    // Entrar al directorio obligatorioPAvanzada antes de acceder al proyecto
                    dir("${params.PROJECT}") {

                        echo "Contenido del directorio ${params.PROJECT}:"
                        bat('dir /B')

                        echo "Construyendo el proyecto ${params.PROJECT}..."

                        if (params.PROJECT == 'USQL') {
                            bat('python tests.py')
                        } 
                        else if (params.PROJECT == 'PEDIDOS') {
                            // Compilar y ejecutar Main.java
                            bat('javac -Xlint:unchecked src\\main\\java\\org\\example\\Main.java')
                            bat('java -cp src\\main\\java org.example.Main')
                        }
                        else if (params.PROJECT == 'TRIVIA') {
                            bat('python main.py')
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
                        // Agrega aquí los pasos para desplegar tu proyecto
                    }
                }
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
