from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils import translation


def hello(request, args):
    return render_to_response('hello.html', {}, context_instance=RequestContext(request))

def home(request, args):
    return render_to_response('pages/home.html', {})
