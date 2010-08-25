from django.template import loader, RequestContext
from django.http import HttpResponse

def show(request, language, sentence_id):
	t = loader.get_template('pages/sentences.html')
	c = RequestContext(request, {
		'sentence_id': sentence_id,
		'language_used': request.session['django_language']
    })
	return HttpResponse(t.render(c))

