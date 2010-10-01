from django.http import HttpResponse
from django.utils import translation

def hello(request):
    return HttpResponse("Hello World! %s" % translation.get_language())

