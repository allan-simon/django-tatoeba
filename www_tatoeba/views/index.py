from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request, language):
	t = loader.get_template('pages/index.html')
	c = RequestContext(request, {
	})
	return HttpResponse(t.render(c))

