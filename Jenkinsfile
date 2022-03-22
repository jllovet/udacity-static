pipeline {
    agent any
    stages {
        stage('Upload to AWS') {
            steps {
                withAWS(credentials:'aws-static', region:'eu-west-1') {
                    s3Upload(
                        file:'index.html',
                        bucket:'afoiiuhawer98h2395r8hwbnsjdfh9w8euihrnoawhethfp9a8ehwrt04r3uh'
                    )
                }

            }
        }
    }
}
