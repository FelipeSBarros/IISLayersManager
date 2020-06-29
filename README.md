
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

## Deploy

[On Pythonanywhere](https://tutorial.djangogirls.org/pt/deploy/#configurando-o-seu-blog-no-pythonanywhere)
```commandline
pip3.6 install --user pythonanywhere

pa_autoconfigure_django.py https://github.com/<your-github-username>/my-first-blog.git
```

# Updating from github
After pulling changes to github projet, go to pythonanywhere.com and login with the username. Then, access bahs console and update it, like showed above: 
```commandline
cd <your-pythonanywhere-domain>.pythonanywhere.com
git pull
```