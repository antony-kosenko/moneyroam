from django.shortcuts import render

# Create your views here.


def login_view(request):
    return render(request, "accounts/login_page.html")

def registration_view(request):
    return render(request, "accounts/registration_page.html")
