
from django.urls import path

#
#
from apps.core.views import register, reg

from apps.articles.views import add_article_page, admin_dashboard, delArtsAdmin, delete_cat, edit_article_admin, edit_article_page, deleteArticle

#admin url imports
from apps.articles.views import admin_dashboard, manage_articles, add_articles_admin, deleteArticleAdmin,manage_categories, add_cat, delete_cat, edit_cat, delArtsAdmin, edit_admin_prof

#accounts
from apps.articles.views import manage_account


from .views import myaccount,edit_profile, accept_invitation
urlpatterns = [
      path('', accept_invitation, name='accept_invitation'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('reg/', reg, name='reg'),
    path('register/', register, name='register'),
    path('myaccount/', myaccount, name='myaccount'),
    
    
    #User article paths
    path('add_article/', add_article_page, name='add_article'),
    path('edit_article/<str:art_code>/', edit_article_page, name='edit_art'),
    path('delete_article/<str:art_code>/', deleteArticle, name='del_art'),
    
    #ADMIN URLS
    path('admin_dashboard/',admin_dashboard, name='admin_dashboard'), #for dashboard
    
    path('manage_articles/',manage_articles, name='manage_articles'), #to manage articles
    path('add_articles_admin/',add_articles_admin, name='add_articles_admin'), #add an article
    path('edit_article_admin/<str:art_code>/', edit_article_admin, name='edit_art_admin'), #edit an article
    path('edit_article_admin/<str:art_code>/', edit_article_admin, name='edit_art_admin'), #edit an article
    path('delete_article_admin/<str:art_code>/', deleteArticleAdmin, name='del_art_admin'), #delete an article
    path('delete_articles_admin/',delArtsAdmin, name='del_arts'), #add an article
    
    
    path('manage_categories/',manage_categories, name='manage_categories'), #manage categories
    path('add_category/', add_cat, name='add_cat'),
    path('add_category/<str:cat_name>/', add_cat, name='add_cat'),
    path('edit_category/', edit_cat, name='edit_cat'), #
    path('delete_category/<int:cat_id>/', delete_cat, name='del_cat'), #
    path('manage_account/', manage_account, name='manage_account'), #
    path('edit_prof/', edit_admin_prof, name='edit_prof'), #
    
    
]
