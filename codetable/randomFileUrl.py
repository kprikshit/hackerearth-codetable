import string
import random

code_url_size = 8

def generateRandomString():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(code_url_size))