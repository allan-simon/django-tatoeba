from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def show(request, sentence_id):
	t = loader.get_template('pages/sentences.html')
	c = RequestContext(request, {
		'sentence_id': sentence_id
    })
	return HttpResponse(t.render(c))

def random(request):
	import random
	r = random.randint(1, 20)
	return HttpResponseRedirect('/en/sentences/show/%i'%r)

