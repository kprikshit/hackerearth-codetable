## How to run this application<br/>
```python
python manage.py makemigrations editor
python manage.py migrate editor
```
### create users for accessing admin website
```python
python manage.py shell
from django.contrib.auth.models import User
user=User.objects.create_user('admin', password='admin')
user.is_active = True
user.is_staff = True
user.is_superuser = True
user.is_authenticated = True
```

### Settings for accessing admin site
```python
python manage.py shell
from django.contrib.sites.models import Site
Site.objects.create(domain='localhost', name='localhost')
Site.objects.create(domain='127.0.0.1', name='127.0.0.1')
```
