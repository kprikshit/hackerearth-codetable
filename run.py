from django.contrib.sites.models import Site
Site.objects.create(domain='localhost', name='localhost')
Site.objects.create(domain='127.0.0.1', name='127.0.0.1')
from django.contrib.auth.models import User
user=User.objects.create_user('admin', password='admin')
user.is_active = True
user.is_staff = True
user.is_superuser = True
user.is_authenticated = True
user.save()

