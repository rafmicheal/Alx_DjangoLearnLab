from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.forms import Textarea
from .models import CustomUser

# Optional: customize the form in admin


class CustomUserAdminForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
        widgets = {
            'bio': Textarea(attrs={'rows': 3, 'cols': 40}),
        }


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserAdminForm
    list_display = ['username', 'email',
                    'date_of_birth', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {
         'fields': ('email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff',
         'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ['username', 'email']
    ordering = ['username']


admin.site.register(CustomUser, CustomUserAdmin)
