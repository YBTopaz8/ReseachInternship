from django.db import models
from django.contrib.auth.models import User

from django.templatetags.static import static

from apps.team.models import Team
from django.contrib.auth.models import User
# Create your models here.



class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name= 'userprofile',  on_delete=models.CASCADE )
    #user = models.CharField( max_length=50)
    active_team_id = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='uploads/avatars/', blank=True, null=True)
    is_leader = models.BooleanField(default=False)
    
    def get_avatar(self):
        if self.avatar:
            return self.avatar.url 
        else:
          #'  return 'static/images/user.png'
            return static("images/user.png")
    
    def get_team_name(self):
        name = list(Team.objects.filter(id=self.active_team_id).values_list('title', flat=True).distinct())
        #print(name[0])
        return f'{name[0]}'
    
    def __str__(self):
      
        return f'{self.user.username } ({self.user.first_name} {self.user.last_name})'
    