from django.contrib import admin
from curdapp.models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','password')


