pipeline {
  agent any
  stages {
    stage('Login ') {
      steps {
        sh './clean.sh'
      }
    }

    stage('Prueba Navegadores') {
      parallel {
        stage('Prueba Navegadores') {
          steps {
            sh './abrirnavegadores.sh'
          }
        }

        stage('Firefox') {
          steps {
            sh './abrirfirefox.sh'
          }
        }

        stage('Chrome') {
          steps {
            sh './abrirchrome.sh'
          }
        }

        stage('IExplorer') {
          steps {
            sh './abrirexplorer.sh'
          }
        }

        stage('Safari') {
          steps {
            sh './abrirsafari.sh'
          }
        }

        stage('Opera') {
          steps {
            sh './abriropera.sh'
          }
        }

      }
    }

    stage('CRUD') {
      parallel {
        stage('CRUD') {
          steps {
            sh './ejeutarcrud.sh'
          }
        }

        stage('Insertar Registro') {
          steps {
            sh './insertarregistro.sh'
          }
        }

        stage('Actualizar Registro') {
          steps {
            sh './actualizarregistro.sh'
          }
        }

        stage('Consultar Registro') {
          steps {
            sh './consultarregistro.sh'
          }
        }

        stage('Eliminar Registro') {
          steps {
            sh './eliminarregistro.sh'
          }
        }

      }
    }

    stage('Exportar Reporte') {
      steps {
        sh './exportarreporte.sh'
      }
    }

    stage('Desplegar') {
      steps {
        sh './desplegar.sh'
      }
    }

  }
}