from django.conf.urls import url
from . import editorViews

urlpatterns = [
    url(r'^$', editorViews.editor_blank_redirect, name='Blank'),
    url(r'^save/$', editorViews.save, name='Save'),
    url(r'^generate/$', editorViews.generate, name='Save'),
    url(r'^starter/$', editorViews.get_starter_code, name='CodeText'),
    url(r'^(?P<code_id>\w+)/', editorViews.new_code, name='CodeId'),
]
