from django.conf import settings
import random
import string
SHORTCODE_MIN = getattr(settings,"SHORTCODE_MIN",6)
def code_generator(size=SHORTCODE_MIN,chars=string.ascii_lowercase+ string.ascii_uppercase +string.digits):
    newCode=""
    for _ in range(size):
        newCode += random.choice(chars)
    return newCode

def create_shortcode(instance,size=SHORTCODE_MIN):
    newshortcode = code_generator(size)
    Klass_simpleURL = instance.__class__
    qs_exists  = Klass_simpleURL.objects.filter(shortcode=newshortcode).exists()
    if qs_exists :
        return create_shortcode(size=size)
    return newshortcode
