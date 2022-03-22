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
                        bucket:'afoiiuhawer98h2395r8hwbnsjdfh9w8euihrnoawhethfp9a8ehwrt04r3uh'
                    )
                }
            }
        }
    }
}
