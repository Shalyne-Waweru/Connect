from django.shortcuts import render

# Create your views here.

def index(request):
  '''
  View function that renders the landing page and its data
  '''
  return render(request, 'index.html')