from django.contrib import admin
from .the_models import Users


class AdminDisplayUsers(admin.ModelAdmin):
    list_display = [
        'user_id', 'full_name', 'email', 'phone']


admin.site.register(Users, AdminDisplayUsers)

