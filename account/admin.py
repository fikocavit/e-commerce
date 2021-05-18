from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display=('email','username','first_name','data_joined','is_active')
    list_display_links=('email','username','first_name')
    readonly_fields=('last_login','data_joined')
    ordering=('-data_joined',)
    
    
    filter_horizontal=()
    list_filter=()
    fieldsets=()
    


admin.site.register(Account,AccountAdmin)