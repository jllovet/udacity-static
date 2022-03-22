pipeline {
    agent any
    stages {
        stage('Lint HTML') {
            steps {
                sh 'tidy -q -e *.html'
            }
        }
        stage('Upload to AWS') {
            steps {
                withAWS(credentials:'aws-static', region:'us-east-2') {
                    s3Upload(
                        file:'index.html',
                        bucket:'<bucket-name>'
                    )
                }
            }
        }
    }
}
