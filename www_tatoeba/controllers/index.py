from django.http import HttpResponse
from django.template import Context, loader

def index(request):
	t = loader.get_template("skeleton.html")
	c = Context({
		'title': 'Tatoeba: Collecting example sentences',
		'page': 'pages/index.html'
	})
	return HttpResponse(t.render(c))

