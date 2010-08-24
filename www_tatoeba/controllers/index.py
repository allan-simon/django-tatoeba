from django.http import HttpResponse
from django.template import Context, loader

def index(request):
	t = loader.get_template("skeleton.html")
	c = Context({
		'title': 'Tatoeba: Collecting example sentences',
		'page': 'index.html'
	})
	return HttpResponse(t.render(c))

