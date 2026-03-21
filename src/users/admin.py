from django.contrib import admin

from users.models import City, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "id")
    search = ("username", "email")
    readonly_fields = ("created_at", "updated_at")
    autocomplete_fields = ("city",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    search_fields = ("name",)
