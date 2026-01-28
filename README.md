# churn
# churn

commands

Step 2: Create Virtual Environment
python -m venv venv
source venv/bin/activate

Activate the virtual environment in windows
Command Prompt (cmd):
venv\Scripts\activate


PowerShell:
venv\Scripts\Activate.ps1

Open PowerShell as Administrator and run:
winget install --id GitHub.cli

gh --version
gh auth login

fast api command run from root dircetory which is churn/
uvicorn app.main:app --host 0.0.0.0 --port 8000


docker build cmd run from root directory which is churn/
docker build -t ml-api .
docker run -p 8000:8000 ml-api


aws configure
: past access key and secret key
aws sts get-caller-identity
