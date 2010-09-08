from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
	t = loader.get_template('pages/index.html')
	c = RequestContext(request, {})
	return HttpResponse(t.render(c))

def home(request):
	t = loader.get_template('pages/home.html')
	c = RequestContext(request, {})
	return HttpResponse(t.render(c))

