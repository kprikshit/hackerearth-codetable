from django.conf.urls import url
from . import editorViews

urlpatterns = [
    url(r'^$', editorViews.editor_blank_redirect, name='Blank'),
    url(r'^save/$', editorViews.save, name='Save'),
    url(r'^(?P<code_id>\w+)/', editorViews.new_code, name='CodeId'),    
]
