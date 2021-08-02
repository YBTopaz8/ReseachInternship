from apps.articles.models import Articles
from django.core.mail.message import EmailMultiAlternatives
from django.http.response import HttpResponse
from apps.team.utilities import send_invitation_accepted
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.contrib.auth.models import User

from .models import Userprofile
from apps.team.models import Invite, Team


#views



@login_required
def myaccount(request):
    teams = request.user.teams.exclude(pk=request.user.userprofile.active_team_id)
    invitations = Invite.objects.filter(email=request.user.email, status=Invite.INVITED)
    articles = Articles.objects.all()
    
    
    return render(request, 'userprofile/myaccount.html',{'teams' : teams, 'invitations':invitations, 'articles':articles})

@login_required
def edit_profile(request):
    
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()
        
        if request.FILES:
            avatar = request.FILES['avatar']
            userprofile = request.user.userprofile
            userprofile.avatar = avatar
            userprofile.save()
        
        messages.info(request, 'The changes were Saved!')    
        return redirect('myaccount')
    
    return render(request, 'userprofile/edit_profile.html')
    


def accept_invitation(request):
    if request.method=='POST':
        code = request.POST.get('code')
        email = request.POST.get('email')
      #  passs = request.POST.get('pass')
        
        print(email)
        print(code)
      #  print(passs)
        invitations = Invite.objects.filter(code=code, email=email)
        
        if invitations:
            
            invitation = invitations[0]
            invitation.status = Invite.ACCEPTED
            invitation.save()
            """
            team = invitation.team
            team.members.add(request.user)
            team.save()
            
            userprofile = request.user.userprofile  
            userprofile.active_team_id = team.id
            userprofile.save()  
            
            messages.info(request, 'Invitations Accepted')
            
            send_invitation_accepted(team, invitation)
            
            #return HttpResponse('<h1>OK</h1>')
            return redirect('team:team', team_id=team.id)
        """
            #return HttpResponse('<h1>OK</h1>')
            
            #'render(request, 'core/signup.html', {})
            return redirect('reg')
        else:
            messages.info(request, 'Invitation was not found')
    else:
        return render(request, 'userprofile/accept_invitation.html')

