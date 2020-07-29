from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, users


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'Mobile_Number', 'select_dept']


admin.site.register(CustomUser, CustomUserAdmin)


class UsersAdmin(admin.ModelAdmin):
    list_display = ['title1', 'no1']


admin.site.register(users, UsersAdmin)
