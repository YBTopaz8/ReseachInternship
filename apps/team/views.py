# Import Django
from django.utils.html import conditional_escape
from apps.userprofile.models import Userprofile
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
# Create your views here.

from .utilities import send_invitation, send_invitation_accepted

from .models import Invite, Team
import random
#
#views




@login_required
def team(request, team_id):
    team = get_object_or_404(Team, pk=team_id, status=Team.ACTIVE, members__in=[request.user])
    invitations= team.invitations.filter(status=Invite.INVITED)
    return render(request, 'team/team.html', {'team': team, 'invitations':invitations})

@login_required
def add(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            team = Team.objects.create(title=title, created_by=request.user)
            team.members.add(request.user)
            team.save()
            
            userprofile = request.user.userprofile
            userprofile.active_team_id = team.id 
            userprofile.save()
            
            return redirect('myaccount')
    return render(request, 'team/add.html')

@login_required
def edit(request):
    team = get_object_or_404(Team, pk=request.user.userprofile.active_team_id, status=Team.ACTIVE, members__in=[request.user])
    if request.method == "POST":
        title = request.POST.get('title')
        
        if title:
            team.title = title
            team.save()
            
            messages.Info(request, 'The Changes Were Saved')
            
            return redirect('team:team', team_id=team.id)
    return render(request, 'team/edit.html', {'team':team})

@login_required
def activate_team(request, team_id):
    team = get_object_or_404(Team, pk=request.user.userprofile.active_team_id, status=Team.ACTIVE, members__in=[request.user])
    userprofile = request.user.userprofile
    userprofile.active_team_id = team_id
    userprofile.save()
    
    messages.info(request, 'The Team Was Activated')
    
    return redirect('team:team', team_id=team_id)

@login_required
def invite(request):
    team = get_object_or_404(Team, pk=request.user.userprofile.active_team_id, status=Team.ACTIVE, members__in=[request.user])

    if request.method == 'POST':   
        email = request.POST.get('email')
        
        if email:
            invitations= Invite.objects.filter(team=team, email=email)
            
            if not invitations:
                code = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890') for i in range(6))
                invitation = Invite.objects.create(team=team, email=email, code=code)
                
                messages.info(request, 'The User was Invited')
                
                send_invitation(email, code, team)
                
                return redirect('team:team', team_id=team.id)
            else:
                messages.info(request, 'The User has already been invited')
                
    return render(request, 'team/invite.html', {'team':team})
