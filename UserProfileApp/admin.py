from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class Userlist(UserAdmin):
    fieldsets = (
        ('Личные данные', {'fields': (('email', 'username'), ('first_name', 'last_name'))}),
        ('Группа и права', {
            'fields': ('groups', 'user_permissions',),
        }),
        ('Служебные данные', {
            'classes': ('collapse',),
            'fields': (
                ('is_superuser', 'is_staff', 'is_active',), 'updated_at', 'created_at', 'last_login', 'password',)}),
    )
    add_fieldsets = (
        ('Личные данные', {'fields': (('username', 'email',), ('first_name', 'last_name'))}),
        ('Пароль', {
            'fields': (('password1', 'password2',),),
        }),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email', 'username',)
    readonly_fields = ('created_at', 'updated_at', )
    list_display = ('username', 'email', 'last_name', 'first_name',)
    list_filter = ('groups', 'is_superuser', 'is_staff', 'created_at',)
