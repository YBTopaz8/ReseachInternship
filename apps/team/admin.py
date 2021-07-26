from apps import team
from django.contrib import admin

# Register your models here.
from .models import Team, Invite

admin.site.register(Team)
admin.site.register(Invite)