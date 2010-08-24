from django.template import Context, loader
from django.http import HttpResponse
from django.utils import translation

def show(request, lang, sentence_id):
	t = loader.get_template('skeleton.html')
	c = Context({
		'title': 'my super title',
		'page': 'pages/sentences.html',
		'sentence_id': sentence_id,
		'language_used': request.session['django_language']
    })
	return HttpResponse(t.render(c))
	#return HttpResponse("Hello, world. Vous regarder la phrase %s." % sentence_id)

