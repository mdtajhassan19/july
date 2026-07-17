pipeline {

    agent any

    environment {
    PYTHON = 'C:\\Users\\tajhassan\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'
    VENV = 'venv'
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
                dir "C:\\Users\\tajhassan\\AppData\\Local\\Programs\\Python\\Python314"
                "C:\\Users\\tajhassan\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" --version
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
                %VENV%\\Scripts\\python.exe -m pip install --upgrade pip
                %VENV%\\Scripts\\python.exe -m pip install -r requirements.txt
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

        // stage('Run Automation') {

        //     steps {

        //         bat """
        //             %VENV%\\Scripts\\python.exe -m pytest tests -v ^
        //             --html=reports/report.html ^
        //             --self-contained-html ^
        //             --alluredir=allure-results ^
        //             --junitxml=reports/junit.xml
        //         """
        //     }

        // }

        stage('Run Automation') {

            steps {

                bat """
                    %VENV%\\Scripts\\python.exe -m pytest tests -v ^
                    --html=reports/report.html ^
                    --self-contained-html ^
                    --alluredir=allure-results
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

        // always {
        //     junit allowEmptyResults: true,
        //       testResults: 'reports/junit.xml'
        // }

        success {

            echo "Build Successful"

        }

        failure {

            echo "Build Failed"

        }

    }

}