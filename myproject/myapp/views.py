from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "index.html")

def book_done(request):
    return render(request, "book_done.html")

def book(request):
    return render(request, "book.html")

def login_done(request):
    return render(request, "login_done.html")

def login(request):
    return render(request, "login.html")

def rooms(request):
    return render(request, "rooms.html")

def signup(request):
    return render(request, "signup.html")


