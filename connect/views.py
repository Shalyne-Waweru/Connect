from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import LoginForm,PostForm
from .email import send_welcome_email
from .models import Post

# Create your views here.

def index(request):
  '''
  View function that renders the landing page and its data
  '''
  return render(request, 'index.html')

def logout(request):
  '''
  View function that logs out the user
  '''
  auth.logout(request)
  messages.success(request,"User Logged Out Successfully!")
  return redirect('loginPage')

def login(request):
    form=LoginForm()

    if request.method=='POST':
        form=LoginForm(request.POST)

        if form.is_valid():
            username  = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user= auth.authenticate(request,username=username,password=password)
            print(user)

            if user is not None:
              auth.login(request, user)
              return redirect('timelinePage')

            else:
              messages.error(request,"Wrong credentials, Please Try Again!")
      
    return render(request, 'registration/login.html', locals())

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
              new_user.is_staff = True
              new_user.save()

              # Sending The Welcome Email Message
              send_welcome_email(username,email)

              if new_user is not None:
                messages.success(request,"User Registered Successfully!")
                return redirect('loginPage')
              
        else:
          messages.error(request,"Passwords Don't Match!")
  
  return render(request, 'registration/signup.html', locals())


def timeline(request):
  '''
  View function that renders the timeline page and its data
  '''

  posts = Post.all_posts()

  form=PostForm()

  if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            image = request.FILES['image']
            caption = request.POST['caption']

            new_post = Post.objects.create(image=image, caption=caption, user=request.user)
            new_post.save()

            print(image)
            print(caption)

            return HttpResponseRedirect(request.path_info)
  else:
      form = PostForm()

  return render(request, 'timeline.html', {"posts": posts})

def profile(request):
  '''
  View function that renders the profile page and its data
  '''
  return render(request, 'profile.html')