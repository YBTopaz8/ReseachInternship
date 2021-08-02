from django.contrib import admin

# Register your models here.
from .models import Articles,Categories

admin.site.register(Articles)
admin.site.register(Categories)