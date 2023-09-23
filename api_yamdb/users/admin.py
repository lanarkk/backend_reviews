from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = (
        'username',
        'email',
        'first_name',
        'last_name',
        'bio',
        'role',
    )
