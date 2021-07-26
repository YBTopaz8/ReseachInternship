
from django.urls import path

#
#
from apps.core.views import register, reg
from .views import myaccount,edit_profile, accept_invitation
urlpatterns = [
      path('', accept_invitation, name='accept_invitation'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('reg/', reg, name='reg'),
    path('register/', register, name='register'),
    path('myaccount/', myaccount, name='myaccount')
    
]
