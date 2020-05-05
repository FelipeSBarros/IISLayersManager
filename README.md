
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
python manage.py makemigrations IIS
python manage.py migrate IIS
python manage.py createsuperuser
```