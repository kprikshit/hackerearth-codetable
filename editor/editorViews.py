from django.http import *
from django.template import loader
from editor.models import Code
from codetable.randomFileUrl import generateRandomString
from languageExtension import *
from constants import *
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import requests
import string
import json


# Database related function
def check_in_database(code_id):
    return Code.objects.filter(pk=code_id).exists()


def insert_into_database(code_id):
    Code.addDefault(Code(), code_id)


def get_from_database(code_id):
    if check_in_database(code_id):
        return Code.objects.get(pk=code_id)
    else:
        return

@csrf_exempt
def generate(request):
    code_id = ""
    if request.method == "POST":
        code_id = request.POST.get('code_id', '')
    else:
        code_id = request.GET.get('code_id', '')
    if code_id == "":
        return HttpResponse("");

    obj = get_from_database(code_id)
    obj.shared = True
    obj.share_url = code_id
    obj.save();

    share_url = get_share_url(request.get_host(), code_id);
    return  HttpResponse(share_url)


def get_share_url(host, code_id):
    return "http://" + host + "/editor/" + code_id +"/"

'''
redirect function for /editor/ to /editor/randomString/
'''
def editor_blank_redirect(request):
    final_url = generateRandomString()
    return HttpResponseRedirect(final_url)


def get_code_text(code_id, code_lang):
    file_name = generateFileName(code_id, code_lang)
    code_obj = open("codes/"+file_name, "r")
    return code_obj.read()

'''
Get the starter code for various language
'''
def get_default_code_text(code_lang):
    if code_lang == DEFAULT_C_NAME:
        return C_STARTER_CODE
    elif code_lang == DEFAULT_CPP_NAME:
        return CPP_STARTER_CODE
    elif code_lang == DEFAULT_CPP11_NAME:
        return CPP11_STARTER_CODE
    elif code_lang == DEFAULT_JAVA_NAME:
        return JAVA_STARTER_CODE
    elif code_lang == DEFAULT_JAVASCRIPT_NAME:
        return JAVASCRIPT_STARTER_CODE
    elif code_lang == DEFAULT_PERL_NAME:
        return PERL_STARTER_CODE
    elif code_lang == DEFAULT_PHP_NAME:
        return PHP_STARTER_CODE
    elif code_lang == DEFAULT_PYTHON_NAME:
        return PYTHON_STARTER_CODE
    elif code_lang == DEFAULT_RUBY_NAME:
        return RUBY_STARTER_CODE
    elif code_lang == DEFAULT_TEXT_NAME:
        return TEXT_STARTER_CODE
    else:
        return TEXT_STARTER_CODE


def get_default_lang_extension(code_lang):
    if code_lang == DEFAULT_C_NAME:
        return C_EXTENSION
    elif code_lang == DEFAULT_CPP_NAME or code_lang == DEFAULT_CPP11_NAME:
        return CPP_EXTENSION
    elif code_lang == DEFAULT_JAVA_NAME:
        return JAVA_EXTENSION
    elif code_lang == DEFAULT_JAVASCRIPT_NAME:
        return JAVASCRIPT_EXTENSION
    elif code_lang == DEFAULT_PERL_NAME:
        return PERL_EXTENSION
    elif code_lang == DEFAULT_PHP_NAME:
        return PHP_EXTENSION
    elif code_lang == DEFAULT_PYTHON_NAME:
        return PYTHON_EXTENSION
    elif code_lang == DEFAULT_RUBY_NAME:
        return RUBY_EXTENSION
    elif code_lang == DEFAULT_TEXT_NAME:
        return TEXT_EXTENSION
    else:
        return TEXT_EXTENSION

@csrf_exempt
def get_starter_code(request):
    code_lang = request.POST.get('lang', '')
    if code_lang =="":
        return HttpResponse("")
    return HttpResponse(get_default_code_text(code_lang))


def new_code(request, code_id):
    template = loader.get_template('base.html')
    presentInDb = check_in_database(code_id)
    code_text = "";
    code_lang = DEFAULT_LANGUAGE;

    #if the code was already present in database
    if presentInDb:
        obj2 = get_from_database(code_id)
        code_lang = obj2.code_lang
        code_text = get_code_text(code_id, code_lang)
    # if the code is not present in database
    else:
        insert_into_database(code_id)
        code_text = DEFAULT_TEXT
        code_lang = DEFAULT_LANGUAGE
    obj = get_from_database(code_id)
    context = {'file_name': code_id, 'code_last_save_date': obj.last_save_date, 'code_create_date': obj.create_date, 'code_text': code_text, 'code_lang': code_lang, 'shared': False}
    if obj.shared:
        context['shared_url'] = get_share_url(request.get_host(), code_id)
        context['shared'] = True
    return HttpResponse(template.render(context, request))


def generateFileName(file_name, code_lang):
    return file_name + get_default_lang_extension(code_lang);


def update_in_database(code_id, curr_date, code_lang):
    code_obj = Code.objects.get(pk=code_id)
    code_obj.last_save_date = curr_date
    code_obj.code_lang = code_lang
    code_obj.save();

@csrf_exempt
def save(request):
    code_lang = request.POST.get('lang', '')
    code_text = request.POST.get('text', '')
    code_id = request.POST.get('id', '')
    try:
        #save the code in the file
        codeFile = open('codes/'+generateFileName(code_id, code_lang), 'w+')
        codeFile.write(code_text);
        codeFile.close();
        save_time = timezone.now();
        # update in database now
        update_in_database(code_id, save_time, code_lang)
        return HttpResponse(str(save_time) );
    except Exception as ex:
        print ex
        return HttpResponse("error in saving file")

def input_to_html(code_input):
    input = code_input;
    if input == "":
        input = "Std input is empty"
    else:
        input = string.replace(input, "\n", "<br/>")
        input = string.replace(input, "\t", "&nbsp;")
    return input


@csrf_exempt
def compile_run(request):
    code_id = request.POST.get('id', '')
    code_input = request.POST.get('input', '');
    if code_id =='':
        return HttpResponse("Empty Id received")
    # get required information
    code_obj = get_from_database(code_id)
    source = get_code_text(code_id, code_obj.code_lang)

    if code_obj.code_lang == DEFAULT_TEXT_NAME:
        return HttpResponse("Text file compile is not yet supported")
    data = {'client_secret': API_CLIENT_SECRET_KEY, 'source': source, 'lang': code_obj.code_lang}
    if code_input != "":
        data['input'] = code_input


    # Make the API request here
    response = requests.post(API_RUN_URL, data = data).json()

    # return the required run data only
    run_data = {}
    run_data['compile_status'] = response['compile_status']
    if response['compile_status'] == "OK":
        run_data['output'] = response['run_status']['output_html']
        run_data['input'] = input_to_html(code_input)

        # transform empty input/output
        if run_data['output'] == "":
            run_data['output'] = "Std output is empty"

        run_data['memory_used'] = response['run_status']['memory_used']
        run_data['time_used'] = response['run_status']['time_used']
        run_data['status'] = response['run_status']['status']
        run_data['status_detail'] = response['run_status']['status_detail']
        run_data['error'] = 0;
    else:
        run_data['error'] = 1;
    return HttpResponse(json.dumps(run_data))