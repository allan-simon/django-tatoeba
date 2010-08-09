from django.template import Context, loader
from django.http import HttpResponse

def show(request, sentence_id):
	t = loader.get_template('sentences.html')
	c = Context({
		'sentence_id': sentence_id,
    })
	return HttpResponse(t.render(c))
	#return HttpResponse("Hello, world. Vous regarder la phrase %s." % sentence_id)
