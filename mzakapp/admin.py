from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_filter = ("contact","last_name")
    list_display = ('last_name', 'first_name', 'contact')
    fields = ['first_name', 'last_name', ('contact', 'email')]

admin.site.register(User,UserAdmin)
