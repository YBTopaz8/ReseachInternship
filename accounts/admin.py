from django.contrib import admin

# Register your models here.
from accounts.models import Invitation_Tables, Users_Table

class Invitation_TablesAdmin(admin.ModelAdmin):
    list_display = ('inv_code', 'inv_code_date',)

class Users_TableAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','username', 'email', 'FK_inv_code','sign_in_date')


admin.site.register(Invitation_Tables, Invitation_TablesAdmin)
admin.site.register(Users_Table, Users_TableAdmin)
