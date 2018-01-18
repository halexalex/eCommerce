from django.shortcuts import render

from .forms import ContactForm


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
    return render(request, 'contact/view.html', context)
