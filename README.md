# IIS Layer Manager

## Developing from github project  

* Clone repo;
```commandline
git clone https://github.com/marcellobenigno/geopocos.git
cd geopocos
```
* Create virtualenv;
```commandline
python -m venv .venv
```
* Activate virtualenv;
```commandline
source .venv/bin/activate
```
* Install dependencies/requirements;
```
pip install -r requirements-dev.txt
```
* Crie o banco de dados espacial como foi descrito acima;
```commandline
python manage.py makemigrations
python manage.py migrate
```
* Run runserver
```commandline
python manage.py runserver
```
* Creating superuser
```
python manage.py createsuperuser
```

# Deploy changes from github
After pulling changes to github project, go to pythonanywhere.com and login with the username.  
Then, access bahs console and update it, like showed above: 
```commandline
cd <your-pythonanywhere-domain>.pythonanywhere.com
git pull
```
