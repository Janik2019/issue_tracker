from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from accounts.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


def login_view(request):
    context = {}
    next = request.GET.get('next')
    request_page = request.session.setdefault('request_page', next)
    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request_page)
        else:
            context['has_error'] = True

    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('webapp:index')


def register_view(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
    elif request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['username'],
                        first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name'],
                        email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect("webapp:index")
        else:
            return render(request, 'register.html', {'form': form})

