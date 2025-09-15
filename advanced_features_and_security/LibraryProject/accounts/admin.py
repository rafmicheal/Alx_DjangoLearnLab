from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django import forms
from django.forms import Textarea


class CustomUserAdminForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
        widgets = {'bio': Textarea(attrs={'rows': 3, 'cols': 40})}


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserAdminForm
    list_display = ['username', 'email',
                    'date_of_birth', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {
         'fields': ('email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff',
         'is_active', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
