from django.contrib import messages
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db import reset_queries
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist

import random
from django.contrib.auth.decorators import login_required
from .forms import Add_article
# Create your views here.
from .models import Articles, Categories

from apps.userprofile.models import Userprofile

@login_required
def add_article_page(request):
    """
    cat=Categories.objects.all().values('name')
    #cov.get_art_cover()
    
    if request.method == 'POST':
        art_code= request.POST.get('art_code', '')
        art_title= request.POST.get('art_title', '')
        art_category= request.POST.get('art_category', '')
        art_publisher= request.POST.get('art_publisher', '')
        art_volume= request.POST.get('art_volume', '')
        art_date= request.POST.get('art_date', '')
        
        print("code is " + art_code)
        print(art_title)
        print(art_category)
        print("publisher is "+ art_publisher)
        print(art_volume)
        print(art_date)
        cat = get_object_or_404(Categories, name=art_category)
        print("category is" + cat)
      
        if request.FILES:
            art_cover=request.FILES['art_cover']
            art_document=request.FILES['art_document']
            #Articles.objects.create(art_cover=art_cover, art_document=art_document)
            Article = Articles.objects.create(art_publisher=request.user,art_title=art_title,
                                          art_code=art_code,art_category=cat,art_volume=art_volume,
                                          art_created_date=art_date, art_cover=art_cover, art_document=art_document)
            Article.save()
            messages.info(request, 'New Book Added!')
            return redirect('myaccount')
    """
    if request.method == 'POST':
            #article= Articles.objects.get(art_code=art_code)
            #print(article)
            art_code= request.POST.get('art_code', '')
            art_title= request.POST.get('art_title', '')
            art_category= request.POST.get('art_category', '')
            art_publisher= request.POST.get('art_publisher', '')
            art_volume= request.POST.get('art_volume', '')
            art_date= request.POST.get('art_date', '')
            art_description= request.POST.get('art_description', '')
            
            print("code is " + art_code)
            print(art_title)
            print(art_category)
            print("publisher is "+ art_publisher)
            print(art_volume)
            print(art_date)
            print(art_description)
            cat = get_object_or_404(Categories, name=art_category)
            print(cat)
            if request.FILES:
                art_cover=request.FILES['art_cover']
                art_document=request.FILES['art_document']
                #Articles.objects.create(art_cover=art_cover, art_document=art_document)
                Article = Articles.objects.create(art_publisher=request.user,art_title=art_title,
                                          art_code=art_code,art_description=art_description,art_category=cat,art_volume=art_volume,
                                          art_created_date=art_date, art_cover=art_cover, art_document=art_document)
                Article.save()
                
                
            # Article.save()
                messages.info(request, 'New Book Added! ')
                return redirect('myaccount')
            else:
                Article = Articles.objects.create(art_publisher=request.user,art_title=art_title,
                                          art_code=art_code,art_description=art_description,art_category=cat,art_volume=art_volume,
                                          art_created_date=art_date)
                #Article.save()
                messages.info(request, 'New Book Added!')
                return redirect('myaccount')
    article=''.join(random.choice('1234567890') for i in range(6))
    cat=Categories.objects.all().values('name')
    context={
        'code':article,
        'cat':cat,
        }

    return render(request, 'articles/add_article.html', context)
    #return redirect('add_article')


"""
this function below (like many others) do 2 stuffs yet.
firstly, it renders the page with the initial intended data (after if )

then there is the if request..... that
    does all the work WHEN the page has to be processed, i.e forms and links
"""
@login_required
def edit_article_page(request, art_code):

    print(art_code)
    
    #print(test.art_category)
    if request.method == 'POST':
            article= Articles.objects.get(art_code=art_code)
            print(article)
            art_code= request.POST.get('art_code', '')
            art_title= request.POST.get('art_title', '')
            art_category= request.POST.get('art_category', '')
            art_publisher= request.POST.get('art_publisher', '')
            art_volume= request.POST.get('art_volume', '')
            art_date= request.POST.get('art_date', '')
            art_description= request.POST.get('art_description', '')

            
            print("code is " + art_code)
            print(art_title)
            print(art_category)
            print(art_description)
            print("publisher is "+ art_publisher)
            print(art_volume)
            print(art_date)
            cat = get_object_or_404(Categories, name=art_category)
            print(cat)
            
            
            """
            essentially here, i did 2 conditions
            if there is any files chosen, it must check BOTH,
            pass them to variables,
            procede to save the article without files
            then extract the model.attribute for file, and assign
            to each file variable , then save. it's basically to update the same instance.
            I didn't use update because it doesn't save in the correct folders
            """
            if request.FILES:
                art_cover=request.FILES['art_cover']
                art_document=request.FILES['art_document']
                #Articles.objects.create(art_cover=art_cover, art_document=art_document)
                articleSave = Articles.objects.filter(art_code=art_code).update(art_publisher=request.user,art_title=art_title,
                                            art_code=art_code,art_category=cat,art_description=art_description,art_volume=art_volume,
                                            art_date=art_date)
                articless= Articles.objects.get(art_code=art_code)
                articless.art_cover=art_cover
                articless.art_document=art_document
                articless.save()
                
                
            # Article.save()
                messages.info(request, 'Book updated! with files')
                return redirect('myaccount')
            else:
                articleSave = Articles.objects.filter(art_code=art_code).update(art_publisher=request.user,art_title=art_title,
                                            art_code=art_code,art_description=art_description,art_category=cat,art_volume=art_volume,
                                            art_date=art_date)
                #Article.save()
                messages.info(request, 'Book updated! without files')
                return redirect('myaccount')
     
    """ TO DELETE AN ARTICLE
    deletee=Articles.objects.get(art_code=art_code)
    deletee.delete()
    """
    article= Articles.objects.get(art_code=art_code)
    print(article.art_category)
    cat=Categories.objects.all().values('name')
    #cov.get_art_cover()
    
    print(article)
    
    context = {
        'article':article,
        'art_code':art_code,
        'cat':cat
    }
    return render(request, 'articles/edit_article.html', context)


def deleteArticle(request, art_code):
    
    deletee=Articles.objects.get(art_code=art_code)
    deletee.delete()
    messages.info(request, 'Book Deleted Successfully! ')
 
    return redirect('myaccount')

#
#
#

""" ADMIN SECTION"""

def admin_dashboard(request):
    articles = Articles.objects.all()
    user = User.objects.all()
    context = {
        'articles':articles,
        'user':user,
    }
    return render(request, 'userprofile/admin/account_index.html', context) 

def manage_articles(request):
    articles = Articles.objects.all()
   
    if request.method == 'POST':
        checkboxIDs = request.POST.getlist('IDss','failed')
        for item in checkboxIDs:
            print(item)
            deleteArticle = Articles.objects.get(art_code=item)
            print(deleteArticle)
            deleteArticle.delete()
        
        return redirect('manage_articles')
    
    context = {
        'articles' : articles
    }
    
    return render(request, 'userprofile/admin/manage_articles.html', context)

def add_articles_admin(request):
  
    if request.method == 'POST':
            #article= Articles.objects.get(art_code=art_code)
            #print(article)
            art_code= request.POST.get('art_code', '')
            art_title= request.POST.get('art_title', '')
            art_category= request.POST.get('art_category', '')
            art_publisher= request.POST.get('art_publisher', '')
            art_volume= request.POST.get('art_volume', '')
            art_date= request.POST.get('art_date', '')
            art_description= request.POST.get('art_description', '')
          
            print("code is " + art_code)
            print(art_title)
            print(art_category)
            print("publisher is "+ art_publisher)
            print(art_volume)
            print(art_date)
            print(art_description)
            
            #to get an instance of cat and user, in order to save them)
            cat = get_object_or_404(Categories, name=art_category)
            print(cat)
            
            pub = get_object_or_404(User, email=art_publisher)
            print(pub)
            
    
            if request.FILES:
                art_cover=request.FILES['art_cover']
                art_document=request.FILES['art_document']
                print(art_cover)
                print(art_document)
                #Articles.objects.create(art_cover=art_cover, art_document=art_document)
                Article = Articles.objects.create(art_publisher=pub,art_title=art_title,
                                          art_code=art_code,art_description=art_description,art_category=cat,art_volume=art_volume,
                                          art_created_date=art_date, art_cover=art_cover, art_document=art_document)
                Article.save()
 
                messages.info(request, 'New Book Added with items!  ')
                return redirect('admin_dashboard')
            else:
                Article = Articles.objects.create(art_publisher=pub,art_title=art_title,
                                          art_code=art_code,art_description=art_description,art_category=cat,art_volume=art_volume,
                                          art_created_date=art_date)
                #Article.save()
                messages.info(request, 'New Book Added!')
                return redirect('admin_dashboard')
    
    article=''.join(random.choice('1234567890') for i in range(6))
    
        
    profile = User.objects.all().values('email')
    print(profile)

    cat=Categories.objects.all().values('name')
    print(cat)
    #profile = User.objects.all()
  #  profile = Userprofile.objects.all()
    context={
        'code':article,
        'cat': cat,
        'profile':profile,
        #'articles':profile
        }
    
    return render(request, 'userprofile/admin/add_article_admin.html',context )

def edit_article_admin(request, art_code):
    print(art_code)
    #catt = get_object_or_404(Articles, art_code=art_code) ONE WAY TO GET CAT
    #print("Cat is " + catt.get_category)
            
    if request.method == 'POST':
        article= Articles.objects.get(art_code=art_code)
        print(article)
        art_code= request.POST.get('art_code', '')
        art_title= request.POST.get('art_title', '')
        art_category= request.POST.get('art_category', '')
        art_publisher= request.POST.get('art_publisher', '')
        art_volume= request.POST.get('art_volume', '')
        art_date= request.POST.get('art_date', '')
        art_description= request.POST.get('art_description', '')

            
        print("code is " + art_code)
        print(art_title)
        print(art_category)
        print(art_description)
        print("publisher is "+ art_publisher)
        print(art_volume)
        print(art_date)
        
        
        cat = get_object_or_404(Categories, name=art_category)
        print(cat)
        
        pub = get_object_or_404(User, email=art_publisher)
        print(pub.id)
            
        """
        essentially here, i did 2 conditions
        if there is any files chosen, it must check BOTH,
        pass them to variables,
        procede to save the article without files
        then extract the model.attribute for file, and assign
        to each file variable , then save. it's basically to update the same instance.
        I didn't use update because it doesn't save in the correct folders
        """
        if request.FILES:
            art_cover=request.FILES['art_cover']
            art_document=request.FILES['art_document']
            #Articles.objects.create(art_cover=art_cover, art_document=art_document)
            articleSave = Articles.objects.filter(art_code=art_code).update(art_publisher=pub,art_title=art_title,
                                        art_code=art_code,art_category=cat,art_description=art_description,art_volume=art_volume,
                                        art_date=art_date)
            articless= Articles.objects.get(art_code=art_code)
            articless.art_cover=art_cover
            articless.art_document=art_document
            articless.save()
                
                
        # Article.save()
            messages.info(request, 'Book updated! with files')
            return redirect('manage_articles')
        else:
            
            articleSave = Articles.objects.filter(art_code=art_code).update(art_publisher=pub,art_title=art_title,
                                        art_code=art_code,art_description=art_description,art_category=cat,art_volume=art_volume,
                                        art_date=art_date)
             #Article.save()
            messages.info(request, 'Book updated! without files')
            return redirect('manage_articles')
    
    
    article= Articles.objects.get(art_code=art_code)
    print(article.art_category)
    print(article.art_date)
    cat=Categories.objects.all().values('name')
    #cov.get_art_cover()
    profile = User.objects.all().values('email')
    print(profile)
    
    print(article)
    context = {
        'article':article,
        'art_code':art_code,
        'cat':cat,
        'profile':profile
    }
    return render(request, 'userprofile/admin/edit_article_admin.html', context) 
    

def deleteArticleAdmin(request, art_code):
    
    deletee=Articles.objects.get(art_code=art_code)
    deletee.delete()
    messages.info(request, 'Book Deleted Successfully! ')
 
    return redirect('manage_articles')


def manage_categories(request):
    cat = list(Categories.objects.all())
    """
    ss= list(Articles.objects.values_list("art_category", flat=True))
    ff = []
    for i in ss:
        if i not in ff:
            ff.append(i)
    for t in range(len(ff)):
        print(t, ff[t])
    num = []
    num1 = []
    
    for item in range(len(ff)):
        g= get_object_or_404(Categories, id=ff[item])
        
        c = Articles.objects.filter(art_category=g.id)
        r= c.count()
        
        num.append(r)
        num1.append(g.name)
        
        print("ID = "+ str(g.id)+ " named " +g.name + " has "+str(c.count()) +" articles"+ " end")
    print(num)
    print(num1)
    for items in cat:
        for item in num1:
            if item == items.name:
                g= get_object_or_404(Categories, name=item)
        
                c = Articles.objects.filter(art_category=g.id)
                r= c.count()
                print(item +" " +str(r) )
            else:
                print(0)
    """
    context = {
        "cat" : cat,
     
        
            
    }
    return render(request, 'userprofile/admin/manage_categories.html',context)

def add_cat(request):
    
    if request.method == 'POST':
        cat_name= request.POST.get('cat_name', '')
        Cat_name_fix=cat_name.replace(" ","_")
        
        print(Cat_name_fix)
        Category = Categories.objects.create(name=Cat_name_fix)
        Category.save()
        messages.info(request, 'New Category Added !  ')
        return redirect('admin_dashboard')
    return render(request, "userprofile/admin/add_cat.html")


def delete_cat(request, cat_name):
    
    test = "Category " + cat_name+ " Deleted successfully"
    deleteCat = Categories.objects.get(name=cat_name)
    deleteCat.delete()
    messages.info(request, test)
    return redirect('manage_categories')

def edit_cat(request, cat_name):
    
    if request.method =='POST':
        cat_name_new= request.POST.get('cat_name_new', '')
        Cat_name_fix=cat_name.replace(" ","_")

        print(Cat_name_fix)
        cat = Categories.objects.filter(name=cat_name).update(name=Cat_name_fix)
        messages.info(request, 'Category name updated !')
        return redirect('manage_categories')
    
    
    print(cat_name)
    context = {
        'name':cat_name
    }
    return render(request, "userprofile/admin/edit_cat.html", context)

def manage_account(request):
    
   
    if request.method == 'POST':
        
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()
        
       
        if request.FILES:
            
            avatar = request.FILES['img']
            userprofile = request.user.userprofile
            userprofile.avatar = avatar
            userprofile.save()
            messages.info(request, 'The changes were Saved with Image Update!')    
            return redirect('manage_account')
        messages.info(request, 'The changes were Saved WITHOUT Image Update!')    
        
        return redirect('manage_account')
        
    
    return render(request, 'userprofile/admin/manage_account.html', {})