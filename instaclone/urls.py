"""instaclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,re_path
from django.contrib.auth import views as auth_view
from connect.views import index,login_user,signup,logout_user,timeline,profile,comment,search_results

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='landingPage'),
    path('login/', login_user, name='loginPage'),
    path('signup/', signup, name='signupPage'),
    path('timeline/', timeline, name='timelinePage'),
    re_path(r'^profile/(\d+)', profile, name='profilePage'),
    path('logout/', logout_user, name='logout'),
    re_path(r'^comment/(?P<post_id>\d+)', comment, name='commentPage'),
    re_path('^search/', search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)