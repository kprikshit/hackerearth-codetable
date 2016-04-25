from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

#Model for storing the file various information about the code file
class Code(models.Model):
    code_name = models.CharField(verbose_name='Code File Name', primary_key=True, max_length=12)
    create_date = models.DateTimeField(verbose_name='Date Created')
    last_save_date = models.DateTimeField(verbose_name='Date Last Saved', null=True, blank=True)
    share_url = models.CharField(verbose_name='Share URL', max_length=12, null=True, blank=True)
    code_lang = models.CharField(verbose_name='Code Language', max_length=10, null=True, blank=True)
    shared = models.BooleanField(verbose_name="Is Shared", default=False)
    
    def addDefault(self, code_id):
        self.create_date = timezone.now()
        self.code_name = code_id;
        self.save()

    def Code(self):
        self.create_date = timezone.now();

    def __str__(self):
        return self.code_name