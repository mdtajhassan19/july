pipeline {

    agent any

    environment {

        PYTHON = "python"
        VENV = "venv"

    }

    stages {

        stage('Checkout') {

            steps {

                checkout scm

            }

        }

        stage('Check Python') {
            steps {
                bat '''
                echo USERNAME=%USERNAME%
                where python
                python --version
                where py
                py --version
                '''
            }
        }

        stage('Create Virtual Environment') {

            steps {

                bat "%PYTHON% -m venv %VENV%"
            }

        }

        stage('Install Dependencies') {

            steps {

                bat """
                call %VENV%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }

        }

        stage('Start FastAPI') {

            steps {

                bat """
                start cmd /c "call %VENV%\\Scripts\\activate && uvicorn app:app --host 127.0.0.1 --port 8000"
                """

                sleep(time:10, unit:'SECONDS')

            }

        }

        stage('Run Automation') {

            steps {

                bat """
                call %VENV%\\Scripts\\activate
                pytest tests -v --html=reports/report.html --self-contained-html --alluredir=allure-results
                """
            }

        }

        stage('Publish HTML Report') {

            steps {

                publishHTML(target: [
                        reportDir: 'reports',
                        reportFiles: 'report.html',
                        reportName: 'Automation Report'
                ])
            }

        }

        stage('Publish Allure') {

            steps {

                allure([
                        includeProperties: false,
                        results: [[path: 'allure-results']]
                ])

            }

        }

    }

    post {

        always {

            junit '**/junit.xml'

        }

        success {

            echo "Build Successful"

        }

        failure {

            echo "Build Failed"

        }

    }

}