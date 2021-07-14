from django.forms.widgets import PasswordInput
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from django.http import HttpResponseRedirect, HttpResponseNotFound

from .forms import CustomUserCreationForm,  InvitationForm

from .models import Invit


def home(request):
   # form = CustomUserCreationForm()
    invitcode = InvitationForm()
    context = {
     #   'form' : form,
        'inv' : invitcode,
    }
    return render(request, 'code.html', context)

def code_val(request):
    sign_in_form = CustomUserCreationForm()
    if request.method =='POST':
        code = request.POST['invCode']
        DB_code_count = Invit.objects.filter(invCode=code).count()
        try:
            DB_code_qty = Invit.objects.get(invCode=code)
            print(code)
            
            print(DB_code_qty)
            context = {
                'form' : sign_in_form,
                'code' : code
            }
        #  return HttpResponse("<h1>test</h1")
            
            if (DB_code_count == 1) and (DB_code_qty.quantity == 1) :
                DB_code_qty.quantity -= 1
                DB_code_qty.save()
                return render(request, 'home.html', context)
                
            else:
                return HttpResponseNotFound('<h1>Le Code a Expirer</h1>')
    
        except Invit.DoesNotExist:
            return HttpResponseNotFound('<h1>Le Code Ne Figure Pas dans la Base De donnee</h1>')


def login_user(request):
    if request.method == 'POST':
       # username = request.POST['username']
        email= request.POST['email']
        password = request.POST['password']
       # code = request.POST['invCode']
        print(password)
        #print(username)
        print(email)
       # print(code)
        """
        form = CustomUserCreationForm(data=request.data)
        if form.is_valid():
            print("valid")
            user = authenticate(email=request.data.get('email'), username=request.data.get('username'), password=request.data.get('password'), )
        """
        user = authenticate(request,email=email,  password=password)
        if user is not None:
            login(request, user)
            print("success")
            return render (request, 'index.html', {})
        else:
            return HttpResponseNotFound('<h1>NO USER </h1>')      
    else:
        return HttpResponseNotFound('<h1>Page Not Found </h1>')  
        

"""
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    """
