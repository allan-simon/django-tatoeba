from django.shortcuts import render_to_response
from django.utils import translation

def hello(request, args):
    return render_to_response('hello.html', {})

