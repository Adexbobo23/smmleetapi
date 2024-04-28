from django.contrib import admin
from .models import UsersReg

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields  = ['first_name', 'last_name' ,'username', 'email']
    list_display  = ['first_name',  'last_name','username', 'email']


admin.site.register(UsersReg, UserAdmin)