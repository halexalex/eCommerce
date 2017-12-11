from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import redirect, render

from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        'title': 'Hello World!',
        'content': 'Welcome to the homepage',
    }
    if request.user.is_authenticated():
        context['premium_content'] = 'YEAHHHHHH!'
    return render(request, 'home_page.html', context)


def about_page(request):
    context = {
        'title': 'About page',
        'content': 'Welcome to the about page',
    }
    return render(request, 'home_page.html', context)


def contact_page(request):
    form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact page',
        'content': 'Welcome to the contact page',
        'form': form,
    }
    if form.is_valid():
        print(form.cleaned_data)
    # if request.method == 'POST':
    #     # print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, 'contact/view.html', context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    print('User logged in')
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # context['forms'] = LoginForm()
            return redirect('/')
        else:
            print('Error')

    return render(request, 'auth/login.html', context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, 'auth/register.html', context)
