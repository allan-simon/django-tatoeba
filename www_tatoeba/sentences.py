from django.http import HttpResponse

def show(request, sentence_id):
	return HttpResponse("Hello, world. Vous regarder la phrase %s." % sentence_id)
