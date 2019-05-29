import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings,"SHORTCODE_MIN",6)

#'abcdefghijklmnopqrstuvwxyz12345567890'
def code_generator(size=SHORTCODE_MIN,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#we need to call the method of class sent. can't use import mehnUrl==circular reference
def create_shortcode(instance,size=SHORTCODE_MIN):
    new_code = code_generator(size)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    #this is recursion. If shortcode still exists, then we call the same function again.
    if qs_exists:
        return create_shortcode(instance,size)
    return new_code
