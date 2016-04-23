from django.shortcuts import render
from django.http import *
from django.template import Context, loader
from django.shortcuts import redirect
from editor.models import Code
from django.utils import timezone
from codetable.randomFileUrl import generateRandomString
from languageExtension import *

# Database related function
def check_in_database(code_id):
	return Code.objects.filter(pk=code_id).exists()

def insert_into_database(code_id):
	Code.addDefault(Code(), code_id);

def get_from_database(code_id):
	if(check_in_database(code_id)):
		return Code.objects.get(pk=code_id)
	else:
		return null;

'''
redirect function for /editor/ to /editor/randomString/
'''
def editor_blank_redirect(request):
    final_url = generateRandomString();
    return HttpResponseRedirect(final_url);

def new_code(request, code_id):
	template = loader.get_template('base.html')
	check = check_in_database(code_id)
	if(check):
		print "already inserted"
	else:
		insert_into_database(code_id)
	obj = get_from_database(code_id);
	context = {'file_name': code_id, 'code_modify_date': obj.last_save_date, 'code_create_date': obj.create_date}
	return HttpResponse(template.render(context, request))	

def generateFileName(name, lang):
	fileName = "";
	if(lang=="C"):
		fileName = name + C_EXTENSION
	elif(lang == "CPP" or lang == "CPP11"):
		fileName = name + CPP_EXTENSION
	elif(lang=="JAVA"):
		fileName = name + JAVA_EXTENSION
	elif(lang=="JAVASCRIPT"):
		fileName = name + JAVASCRIPT_EXTENSION
	elif(lang=="PERL"):
		fileName = name + PERL_EXTENSION
	elif(lang=="PHP"):
		fileName = name + PHP_EXTENSION
	elif(lang=="PYTHON"):
		fileName = name + PYTHON_EXTENSION
	elif(lang=="RUBY"):
		fileName = name + RUBY_EXTENSION
	else:
		fileName = name + TEXT_EXTENSION
	return fileName;



def save(request):
	print 'Lang: ' + request.POST.get('lang','');
	print 'Code: ' + request.POST.get('code','');
	print 'id: ' + request.POST.get('id','');
	print generateFileName(request.POST.get('id',''), request.POST.get('lang',''))
	return HttpResponse("received received");