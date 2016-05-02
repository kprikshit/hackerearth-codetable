## CodeTable
A custom implmentation of HackerEarth's tool CodeTable (https://code.hackerearth.com)<br/>
Code Compilation and Run occurs through HackerEarth's API (https://www.hackerearth.com/docs/api/developers/code/v3/)

### Features
1. Auto Code Saving
2. Online Compile and Run
3. Custom Test Input 
4. Share code
5. Multi Language Support (C,C++, C++11, PYTHON, JAVA, JAVASCRIPT, PHP, RUBY)

This uses Python Django to run the app

### How to run this application<br/>
```python
python manage.py makemigrations editor
python manage.py migrate
```
### create users for accessing admin website
```python
python manage.py shell
from django.contrib.auth.models import User
user=User.objects.create_user('admin', password='admin')
user.is_active = True
user.is_superuser = True
user.is_staff = True
user.is_authenticated = True
user.save()
```

### Settings for accessing admin site
```python
python manage.py shell
from django.contrib.sites.models import Site
Site.objects.create(domain='localhost', name='localhost')
Site.objects.create(domain='127.0.0.1', name='127.0.0.1')
```
