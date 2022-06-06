from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def index(request):
  '''
  View function that renders the landing page and its data
  '''
  return render(request, 'index.html')

def login(request):
  '''
  View function that renders the login page and its data
  '''
  return render(request, 'registration/login.html')

def signup(request):
  '''
  View function that renders the signup page and its data
  '''

  if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        passwordConfirm = request.POST['passwordConfirm']

        if password == passwordConfirm:

            if User.objects.filter(username=username).exists():
              messages.error(request,"Username Already Taken!")

            if User.objects.filter(email=email).exists():
              messages.error(request,"Email Already Taken!")

            else:
              new_user = User.objects.create(username=username, email=email, password=password)
              new_user.save()

              messages.success(request,"User Registered Successfully!")
              return redirect(login)
              
        else:
          messages.error(request,"Passwords Don't Match!")
  
  return render(request, 'registration/signup.html', locals())


def timeline(request):
  '''
  View function that renders the timeline page and its data
  '''
  return render(request, 'timeline.html')

def profile(request):
  '''
  View function that renders the profile page and its data
  '''
  return render(request, 'profile.html')