pipeline {
    agent any

    // Parámetro para seleccionar el proyecto a construir
    parameters {
        choice(name: 'PROJECT', choices: ['usql', 'pedidos', 'trivia'], description: 'Seleccione el proyecto a ejecutar')
    }

    stages {
        // Instalar dependencias según el proyecto seleccionado
        stage('Verificar Python') {
            steps {
                script {
                    bat('where python') // Muestra la ruta de python.exe encontrada
                    bat('python --version')
                }
            }
        }

        stage('Instalar dependencias') {
            steps {
                script {
                    // Cambiar al directorio del proyecto seleccionado
                    dir("obligatorioPAvanzada/${params.PROJECT}") {
                        // Verificar cuál es el proyecto seleccionado y ejecutar los comandos correspondientes
                        if (params.PROJECT == 'usql') {
                            echo "Instalando dependencias para USQL..."
                            bat ('python -m pip install ply') // Instalar PLY para análisis léxico

                        } else if (params.PROJECT == 'trivia') {
                            echo "Instalando dependencias para Trivia..."
                            bat('python -m pip install pandas') // Instalar Pandas para manejo de datos

                        } else if (params.PROJECT == 'pedidos') {
                            echo "No se requieren dependencias adicionales para Pedidos"
                        }
                    }
                }
            }
        }

        // Compilar y construir el proyecto seleccionado
        stage('Build') {
            steps {
                script {
                    dir("obligatorioPAvanzada/${params.PROJECT}") {
                        echo "Construyendo el proyecto ${params.PROJECT}..."

                        // Ejecutar comandos específicos para cada proyecto
                        if (params.PROJECT == 'USQL') {
                            bat('python main.py') // Ejecutar el script principal de USQL

                        } else if (params.PROJECT == 'PEDIDOS') {
                            bat('javac -Xlint:unchecked Main.java') // Compilar el proyecto Java
                            bat('java Main') // Ejecutar el proyecto Java

                        } else if (params.PROJECT == 'TRIVIA') {
                            bat('python main.py') // Ejecutar el script principal de Trivia
                        }
                    }
                }
            }
        }

        // Ejecutar pruebas para el proyecto seleccionado
        stage('Test') {
            steps {
                script {
                    dir("obligatorioPAvanzada/${params.PROJECT}") {
                        echo "Ejecutando pruebas para el proyecto ${params.PROJECT}..."

                        // Ejecutar pruebas específicas según el proyecto
                        if (params.PROJECT == 'USQL') {
                            bat('python Test.py') // Ejecutar pruebas para USQL

                        } else if (params.PROJECT == 'TRIVIA') {
                            bat('python -m unittest') // Ejecutar pruebas unitarias para Trivia

                        } else if (params.PROJECT == 'PEDIDOS') {
                            echo "No se definieron pruebas para Pedidos"
                        }
                    }
                }
            }
        }

        // Despliegue del proyecto seleccionado
        stage('Deploy') {
            steps {
                script {
                    dir("obligatorioPAvanzada/${params.PROJECT}") {
                        echo "Desplegando el proyecto ${params.PROJECT}..."

                        // Ejecutar comandos de despliegue según el proyecto
                        if (params.PROJECT == 'USQL') {
                            echo "Despliegue para USQL no implementado aún"

                        } else if (params.PROJECT == 'TRIVIA') {
                            echo "Despliegue para Trivia no implementado aún"

                        } else if (params.PROJECT == 'PEDIDOS') {
                            echo "Despliegue para Pedidos no implementado aún"
                        }
                    }
                }
            }
        }
    }


}
