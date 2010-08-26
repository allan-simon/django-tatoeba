from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as dlogout

def check_login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			msg = 'login'
		else:
			msg = 'disabled'
	else:
		msg = 'wrong'
	t = loader.get_template('pages/index.html')
	c = RequestContext(request, {})
	return HttpResponse(msg)

def logout(request):
	dlogout(request)
	return HttpResponse('Adieux')
