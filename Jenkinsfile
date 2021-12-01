echo "---build start---"

node {
    stage('PreBuild Stage') {
        echo "---PreBuild Stage---"
        sh 'python3 -m venv .venv'
        source .venv/bin/activate
        sh 'python3 -m pip install -r requirements.txt'
    }

    stage('Test Stage') {
        echo "---Test Stage---"
        sh 'python3 -m unittest discover -v -p "*tests.py"'
    }

    stage('Push Stage') {
        echo "---Push Stage---"
        deactivate
    }
}
