from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "user", "created", "updated", "is_active")
    list_filter = ("user", "created", "updated", "is_active")
    search_fields = ["first_name", "last_name"]
