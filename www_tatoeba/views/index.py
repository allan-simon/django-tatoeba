from django.http import HttpResponse
from django.template import Context, loader

def index(request):
	t = loader.get_template("pages/index.html")
	c = Context({
	})
	return HttpResponse(t.render(c))

