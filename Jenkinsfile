echo "---build start---"

node {
    stage('Pre Git Clone Stage') {
        dir('tests') {
            if(fileExists("/")) {
                sh 'rm -rf tests'
            }
        }
    }
    stage('Git Clone Stage') {
        sh 'mkdir -p tests'
        dir('tests') {
            git branch: 'feature', credentialsId: '2b923bf5-296f-4cc2-a264-1759c48b3be9', url: 'https://github.com/MinJunsu/space-invader.git'
        }
    }
    stage('PreBuild Stage') {
        echo "---PreBuild Stage---"
        dir('tests') {
            sh 'python3 -m venv .venv'
            sh '. .venv/bin/activate'
            sh 'python3 -m pip install -r requirements.txt'
        }
    }

    stage('Test Stage') {
        echo "---Test Stage---"
        dir('tests') {
            sh 'python3 -m unittest discover -v -p "*tests.py"'
        }
    }

    stage('Push Stage') {
        echo "---Push Stage---"
        sh 'rm -rf tests'
    }
}
