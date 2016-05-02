# File extension for various code langauges
C_EXTENSION = ".c"
CPP_EXTENSION = ".cpp"
CPP11_EXTENSION = ".cpp"
JAVA_EXTENSION = ".java"
JAVASCRIPT_EXTENSION = ".js"
PERL_EXTENSION = ".pl"
PHP_EXTENSION = ".php"
PYTHON_EXTENSION = ".py"
RUBY_EXTENSION = ".rb"
TEXT_EXTENSION = ".txt"

# Starter code for various languages
C_STARTER_CODE = '#include <stdio.h>\n\nint main(){\n\tprintf("%s", "Hello World!"");\n\treturn 1;\n}'
CPP_STARTER_CODE = '#include<iostream>\nusing namespace std;\n\nint main(){\n\tcout << "Hello World!!!" << endl;\n\treturn 0;\n}'
CPP11_STARTER_CODE = '#include<iostream>\nusing namespace std;\n\nint main(){\n\tcout << "Hello World!!!" << endl;\n\treturn 0;\n}'
JAVA_STARTER_CODE = "class TestClass {\n\tpublic static void main(String args[] ) throws Exception {\n\t\tSystem.out.println('Hello World!');\n\t}\n}"
JAVASCRIPT_STARTER_CODE = "function func1(){\n\tconsole.log('hello world');\t}"
PERL_STARTER_CODE = "insert perl code here"
PHP_STARTER_CODE = "<?php\necho 'Hello World!';\n?>"
PYTHON_STARTER_CODE = "print 'Hello World!'"
RUBY_STARTER_CODE = "ruby code here"
TEXT_STARTER_CODE = "this is a text file"


DEFAULT_LANGUAGE = "CPP"
DEFAULT_TEXT = CPP_STARTER_CODE


# Default languages and their codes to be used in compile api and in drop-down list on home page
DEFAULT_CPP_NAME = "CPP"
DEFAULT_C_NAME = "C"
DEFAULT_CPP11_NAME = "CPP11"
DEFAULT_JAVA_NAME = "JAVA"
DEFAULT_JAVASCRIPT_NAME = "JAVASCRIPT"
DEFAULT_PERL_NAME = "PERL"
DEFAULT_PHP_NAME = "PHP"
DEFAULT_PYTHON_NAME = "PYTHON"
DEFAULT_RUBY_NAME = "RUBY"
DEFAULT_TEXT_NAME = "TEXT"
