
#
from django.http.response import HttpResponse, HttpResponseNotFound
from apps.team.models import Invite
from apps.userprofile.models import Userprofile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from apps.userprofile.models import Userprofile
#Import functionalities from Django
from django.shortcuts import render,redirect

from apps.articles.models import Categories, Articles

# Create your views here.
def frontpage(request):
    categories = Categories.objects.all()
    articles = Articles.objects.all()
    context = {
        'categories':categories,
        'articles' : articles
    }
    
    return render(request, 'core/frontpage1.html', context)

def privacy(request):
    return render(request, 'core/privacy.html')

def terms(request):
    return render(request, 'core/terms.html')

def plans(request):
    return render(request, 'core/plans.html')

def code(request):
   # form = UserCreationForm(request.POST)
    if request.user.is_authenticated:
        return redirect('myaccount')
    else:
        return render(request, 'userprofile/accept_invitation.html')

           
def reg(request):
        
    return render(request, 'core/signup.html')

def register(request):
    
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        
        #render(request, 'core/signup.html')
        print("testt")
        
        if form.is_valid():
            user = form.save()
            email= form.cleaned_data['username']
            passs= request.POST.get('password1')
            
            print(email)
           
            print(passs)
            
            user.email = user.username
            user.save()
            
            userprofile = Userprofile.objects.create(user=user)
            userprofile.save()
            login(request, user)
           # print(passs)
           # invitations = Invite.objects.filter(email=email, status=Invite.INVITED)
            
         
          #  if invitations:
                #return redirect('accept_invitation')
           #     print(email)
                
        return redirect('myaccount')
            #    render(request,'userprofile/accept_invitation.html', context )
            #    return redirect('accept_invitation')
                
    else:
                #return redirect('dashboard')
             #   print(invitations)
        print("testtErr")
        return HttpResponseNotFound('<h2>NOT INVITED</h2>')
            
           # return redirect('frontpage')"""
  #  else:
       # print("testtTOO")
            #form = UserCreationForm
      #      return HttpResponseNotFound('not a POST')
      #  return redirect('frontpage')
       # return render(request, 'core/signup.html', {'form': form})
