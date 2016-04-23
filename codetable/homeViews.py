from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from randomFileUrl import generateRandomString

'''
Redirect home page to /editor/randomString
'''
def home_redirect(request):
    final_url = "editor/" + generateRandomString();
    return HttpResponseRedirect(final_url);