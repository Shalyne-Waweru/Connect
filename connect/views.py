from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,PostForm,UpdateUserInfoForm,UpdateProfileForm
from .email import send_welcome_email
from .models import Post, Profile
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
  '''
  View function that renders the landing page and its data
  '''
  return render(request, 'index.html')

def logout_user(request):
  '''
  View function that logs out the user
  '''
  logout(request)
  messages.success(request,"User Logged Out Successfully!")
  return redirect('loginPage')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user= authenticate(request,username=username,password=password)
        print (user)

        if user is not None:
            login(request,user)
            return redirect('timelinePage')

        else:
            messages.error(request,"Wrong credentials, Please Try Again!")
    
    return render (request,'registration/login.html', {})

def signup(request):
  '''
  View function that renders the signup page and its data
  '''

  signupForm = SignUpForm()

  if request.method == 'POST':
    signupForm = SignUpForm(request.POST)

    if signupForm.is_valid():
      username = signupForm.cleaned_data['username']
      email = signupForm.cleaned_data['email']

      signupForm.save()

      # Sending the welcome email
      send_welcome_email(username,email)

      messages.success(request, "User Registered Successfully!")
      return redirect("loginPage")

    else:
      messages.error(request, "Password Doesn't Meet the Requirements, Please Try Again!")
      return redirect("signupPage")
    
  else:
    signupForm = SignUpForm()

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

def profile(request, profile_id):
  '''
  View function that renders the profile page and its data
  '''

  myPosts = request.user.posts.all()

  user_info_form = UpdateUserInfoForm()
  update_profile_form = UpdateProfileForm()

  if request.method == 'POST':
    user_info_form = UpdateUserInfoForm(request.POST,instance=request.user)
    update_profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

    if user_info_form.is_valid and update_profile_form.is_valid():
            
            user_info_form.save()
            update_profile_form.save()

            return HttpResponseRedirect(request.path_info)
  else:
        user_info_form = UpdateUserInfoForm(instance=request.user)
        update_profile_form = UpdateProfileForm(instance=request.user.profile)

  return render(request, 'profile.html', locals())