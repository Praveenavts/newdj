from django.contrib import admin
from .models import HomeImage


@admin.register(HomeImage)
class HomeImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title',)
