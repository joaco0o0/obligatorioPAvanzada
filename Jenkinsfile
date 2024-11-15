pipeline {
    agent any
    parameters {
        choice(name: 'PROJECT', choices: ['USQL', 'PEDIDOS', 'TRIVIA'], description: 'Seleccione el proyecto a ejecutar')
    }
    stages {

        stage('Build') {
            steps {
                script {
                    dir("obligatorioPAvanzada/${params.PROJECT}") {

                        echo "Construyendo el proyecto ${params.PROJECT}..."
                        if (params.PROJECT == 'USQL') {
                            sh ('python tests.py')
                        } 
                        else if (params.PROJECT == 'PEDIDOS') {
                            sh('javac -Xlint:unchecked Main.java')
                            sh('java Main')
                        }

                        else if (params.PROJECT == 'TRIVIA') {
                            sh ('python main.py')
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