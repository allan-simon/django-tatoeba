from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate
from django.contrib.auth import login as dlogin
from django.contrib.auth import logout as dlogout


def check_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            dlogin(request, user)
            msg = 'login'
        else:
            msg = 'disabled'
    else:
        msg = 'wrong'
    t = loader.get_template('pages/index.html')
    c = RequestContext(request, {})
    return HttpResponseRedirect('/home')


def logout(request):
    dlogout(request)
    return HttpResponseRedirect('/users/login')


def all(request):
    from www_tatoeba.models import AuthUser
    allUsers = AuthUser.objects.all()
    t = loader.get_template('users/all.html')
    c = RequestContext(request, {
        'allUsers': allUsers
    })
    return HttpResponse(t.render(c))


def register(request):
    from www_tatoeba.forms import RegisterForm
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            from django.contrib.auth.models import User
            user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password']
            )
            return HttpResponseRedirect('/users/login')
    else:
        form = RegisterForm()

    t = loader.get_template('users/register.html')
    c = RequestContext(request, {'form': form})
    return HttpResponse(t.render(c))


def login(request):
    from www_tatoeba.forms import LoginForm
    if request.method == 'POST':
        form = LoginForm(request.POST)
    else:
        form = LoginForm()
    t = loader.get_template('users/login.html')
    c = RequestContext(request, {'form': form})
    return HttpResponse(t.render(c))


def new_password(request):
    #from www_tatoeba.models import AuthUser
    #user = AuthUser.objects.get(email='biptaste@gmail.com')
    t = loader.get_template('users/new_password.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))
