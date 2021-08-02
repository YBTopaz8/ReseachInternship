from django.db import models
from django.contrib.auth.models import User

from django.templatetags.static import static

# Create your models here.



class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name= 'userprofile',  on_delete=models.CASCADE )
    #user = models.CharField( max_length=50)
    active_team_id = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='uploads/avatars/', blank=True, null=True)
    
    def get_avatar(self):
        if self.avatar:
            return self.avatar.url 
        else:
          #'  return 'static/images/user.png'
            return static("images/user.png")
        
    
    def __str__(self):
      
        return f'{self.user.username } ({self.user.first_name} {self.user.last_name})'
    