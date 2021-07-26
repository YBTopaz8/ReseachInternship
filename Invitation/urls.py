"""Invitation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from os import name
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.conf import include

from apps.core.views import frontpage,privacy, terms,plans,code
from apps.userprofile.views import accept_invitation

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('terms/', terms, name='terms'),
    path('privacy/', privacy, name='privacy'),
    path('plans/', plans, name='plans'),
    path('admin/', admin.site.urls),
    
    #
    #Dashboard
    
      path('myaccount/', include('apps.userprofile.urls')), 
      path('myaccount/teams/', include('apps.team.urls')), 
    #
    #Auth
    
    #path('sign/', include('apps.userprofile.urls')),
    path('signup/', code, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html' ), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
