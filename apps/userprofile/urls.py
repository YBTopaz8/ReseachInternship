
from django.urls import path

#
#
from apps.core.views import register, reg

from apps.articles.views import add_article_page, edit_article_page, deleteArticle


from .views import myaccount,edit_profile, accept_invitation
urlpatterns = [
      path('', accept_invitation, name='accept_invitation'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('reg/', reg, name='reg'),
    path('register/', register, name='register'),
    path('myaccount/', myaccount, name='myaccount'),
    
    
    #article paths
    path('add_article/', add_article_page, name='add_article'),
    path('edit_article/<str:art_code>/', edit_article_page, name='edit_art'),
    path('delete_article/<str:art_code>/', deleteArticle, name='del_art')
    
]
