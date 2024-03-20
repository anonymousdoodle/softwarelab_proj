
from django.shortcuts import render, redirect

from .models import db1


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Perform any necessary validation here

        # Save data to the database
        db1.objects.create(username=username, email=email, password=password)
        return redirect('home')  # Redirect to the home page after successful signup
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Perform login validation here

        # Check if the user exists in the database
        user_exists = db1.objects.filter(email=email, password=password).exists()
        if user_exists:
            # Redirect to the home page or any other page after successful login
            return redirect('home')
        else:
            # Handle invalid login
            # You can render a login error message in the login.html template
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')



# def home(request):
    #num_books = 10
    #num_instances = 20
    #num_instances_available = 15
    #num_authors = 5
    #return render(request, 'flashlearn_app/templates/homepage.html', {'num_books': num_books, 'num_instances': num_instances, 'num_instances_available': num_instances_available, 'num_authors': num_authors})