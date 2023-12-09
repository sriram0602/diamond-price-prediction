echo [$(date)]: "START"


echo [$(date)]: "creating env with python 3.8 version" 

virtualenv ./env

echo [$(date)]: "activating the environment" 

source ./env/Scripts/activate

echo [$(date)]: "installing the dev requirements" 

pip install -r requirements.txt

echo [$(date)]: "END" 