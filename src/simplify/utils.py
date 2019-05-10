import random
import string
def code_generator(size=6,chars=string.ascii_lowercase+ string.ascii_uppercase +string.digits):
    newCode=""
    for _ in range(size):
        newCode += random.choice(chars)
    return newCode

def create_shortcode(instance,size= 6):
    newshortcode = code_generator(size)
    Klass_simpleURL = instance.__class__
    qs_exists  = Klass_simpleURL.object.filter(shortcode=newshortcode).exists()
    if qs_exists :
        return create_shortcode(size=6)
    return newshortcode
