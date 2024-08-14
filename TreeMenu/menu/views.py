from django.shortcuts import render


def menu(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def team(request):
    return render(request, 'team.html')


def history(request):
    return render(request, 'history.html')


def services(request):
    return render(request, 'services.html')


def maintenance(request):
    return render(request, 'maintenance.html')


def consulting(request):
    return render(request, 'consulting.html')


def contact(request):
    return render(request, 'contact.html')
