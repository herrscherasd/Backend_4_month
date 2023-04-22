from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.forms import GeekUserCreationForm, GeekUserChangeForm
from users.models import GeekUser

class GeekUserAdmin(UserAdmin):
    add_form = GeekUserCreationForm
    form = GeekUserChangeForm
    model = GeekUser
    list_display = ("email", "is_staff", "is_active")
    list_editable = ("is_active",)
    list_filter = ("email", "is_staff", "is_active")
    ordering = ("email",)
    search_fields = ("email",)
    fieldsets = (
        ("Основная информация", {"fields": ("email", "password")}),
        ("Права доступа", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("Группы и ограничения", {"fields": ("groups", "user_permissions")}),
    )
    add_fieldsets = (
        ("Создание пользователя", {
            'classes' : ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_active", "groups", "user_permissions")}
        ),
    )

admin.site.register(GeekUser,GeekUserAdmin)