from django.shortcuts import render

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
  return render(request, 'registration/signup.html')

def timeline(request):
  '''
  View function that renders the timeline page and its data
  '''
  return render(request, 'timeline.html')