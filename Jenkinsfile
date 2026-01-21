pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\jiban\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" --version'
                bat '"C:\\Users\\jiban\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\jiban\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m pytest'
            }
        }
    }
}
