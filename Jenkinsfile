pipeline {
  agent any
  stages {
    stage('Login ') {
      steps {
        sh '''#!/bin/bash


DIA=`date +"%d/%m/%Y"`
HORA=`date +"%H:%M"`

echo "Se ha logueado el $DIA y la hora actual es $HORA!"'''
      }
    }

    stage('Prueba Navegadores') {
      parallel {
        stage('Prueba Navegadores') {
          steps {
            sh '''#!/bin/bash


DIA=`date +"%d/%m/%Y"`
HORA=`date +"%H:%M"`

echo "Efectuo pruebas de navegador el $DIA y la hora actual es $HORA!"'''
          }
        }

        stage('Firefox') {
          steps {
            sh '''#!/bin/bash


DIA=`date +"%d/%m/%Y"`
HORA=`date +"%H:%M"`

echo "Efectuo pruebas de navegador FIREFOX el $DIA y la hora actual es $HORA!"'''
          }
        }

        stage('Chrome') {
          steps {
            sh '''#!/bin/bash


DIA=`date +"%d/%m/%Y"`
HORA=`date +"%H:%M"`

echo "Efectuo pruebas de navegador GOOGLE CHROME el $DIA y la hora actual es $HORA!"'''
          }
        }

        stage('IExplorer') {
          steps {
            sh '''#!/bin/bash


DIA=`date +"%d/%m/%Y"`
HORA=`date +"%H:%M"`

echo "Efectuo pruebas de navegador INTERNET EXPLORER el $DIA y la hora actual es $HORA!"'''
          }
        }

        stage('Safari') {
          steps {
            sh '''#!/bin/bash


DIA=`date +"%d/%m/%Y"`
HORA=`date +"%H:%M"`

echo "Efectuo pruebas de navegador SAFARI el $DIA y la hora actual es $HORA!"'''
          }
        }

        stage('Opera') {
          steps {
            sh '''#!/bin/bash


DIA=`date +"%d/%m/%Y"`
HORA=`date +"%H:%M"`

echo "Efectuo pruebas de navegador OPERA el $DIA y la hora actual es $HORA!"'''
          }
        }

      }
    }

    stage('CRUD') {
      parallel {
        stage('CRUD') {
          steps {
            sh '''#!/bin/bash


DIA=`date +"%d/%m/%Y"`
HORA=`date +"%H:%M"`

echo "CRUD $DIA y la hora actual es $HORA!"'''
          }
        }

        stage('Insertar Registro') {
          steps {
            sh '''#!/bin/bash


DIA=`date +"%d/%m/%Y"`
HORA=`date +"%H:%M"`

echo "Realizo creación de regsitro  el $DIA y la hora actual es $HORA!"'''
          }
        }

        stage('Actualizar Registro') {
          steps {
            sh '''#!/bin/bash


DIA=`date +"%d/%m/%Y"`
HORA=`date +"%H:%M"`

echo "Realizo actualziación de regsitro  el $DIA y la hora actual es $HORA!"'''
          }
        }

        stage('Consultar Registro') {
          steps {
            sh '''#!/bin/bash


DIA=`date +"%d/%m/%Y"`
HORA=`date +"%H:%M"`

echo "Realizo consulta de registro  el $DIA y la hora actual es $HORA!"'''
          }
        }

        stage('Eliminar Registro') {
          steps {
            sh '''#!/bin/bash


DIA=`date +"%d/%m/%Y"`
HORA=`date +"%H:%M"`

echo "Realizo eliminación de regsitro  el $DIA y la hora actual es $HORA!"'''
          }
        }

      }
    }

    stage('Exportar Reporte') {
      steps {
        sh '''#!/bin/bash


DIA=`date +"%d/%m/%Y"`
HORA=`date +"%H:%M"`

echo "Exporte reporte en excel   el $DIA y la hora actual es $HORA!"'''
      }
    }

    stage('Desplegar') {
      steps {
        sh '''#!/bin/bash


DIA=`date +"%d/%m/%Y"`
HORA=`date +"%H:%M"`

echo "Este es un paso de simulacro de despliegue... NO se ha desplegado 100% - $DIA y la hora actual es $HORA!"'''
      }
    }

  }
}