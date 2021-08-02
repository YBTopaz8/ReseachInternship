from django.contrib import messages
from django.db.models.fields.related import OneToOneField
from django.shortcuts import get_object_or_404, redirect, render

import random
from django.contrib.auth.decorators import login_required
from .forms import Add_article
# Create your views here.
from .models import Articles, Categories

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

    return render(request, 'articles/add_article.html', {'code':article, "cat":cat})
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
    cat=Categories.objects.all().values('name')
    #cov.get_art_cover()
    
    print(article)
    return render(request, 'articles/edit_article.html', {'article':article, 'art_code':art_code, 'cat':cat})


def deleteArticle(request, art_code):
    
    deletee=Articles.objects.get(art_code=art_code)
    deletee.delete()
    messages.info(request, 'Book Deleted Successfully! ')
 
    return redirect('myaccount')