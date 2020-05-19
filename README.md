
```
python -m pip install --upgrade pip
pip install django pandas
```

## Creating project

```
django-admin startproject IISLayersManager .
```

#### Settings
* change timezone
* change lenguage (if necessary)

## Creating app

```commandline
python manage.py startapp iislayers
```

**Após criar o models:**
```
python manage.py migrate
python manage.py makemigrations iislayers
python manage.py migrate iislayers
python manage.py createsuperuser
```