from django.template import Context, loader
from django.http import HttpResponse
from django.utils import translation

def show(request, sentence_id):
	lang = request.GET.get('language', 'fre')
	
	#request.session['django_language'] = lang
	translation.activate(lang) # It work but I think it's better to use LocaleMiddleware
	
	t = loader.get_template('sentences.html')
	c = Context({
		'sentence_id': sentence_id,
		'language_used': lang
    })
	return HttpResponse(t.render(c))
	#return HttpResponse("Hello, world. Vous regarder la phrase %s." % sentence_id)
