from django.template import Context, loader
from django.http import HttpResponse
from django.utils import translation

def show(request, language, sentence_id):
	t = loader.get_template('pages/sentences.html')
	c = Context({
		'sentence_id': sentence_id,
		'language_used': request.session['django_language']
    })
	return HttpResponse(t.render(c))
	#return HttpResponse("Hello, world. Vous regarder la phrase %s." % sentence_id)

