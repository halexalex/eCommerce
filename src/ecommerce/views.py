from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {
        'title': 'Hello World!',
        'content': 'Welcome to the homepage',
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    context = {
        'title': 'About page',
        'content': 'Welcome to the about page',
    }
    return render(request, 'home_page.html', context)


def contact_page(request):
    context = {
        'title': 'Contact page',
        'content': 'Welcome to the contact page',
    }
    return render(request, 'home_page.html', context)


