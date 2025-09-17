from django.contrib import admin
from .models import SearchHistory

@admin.register(SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('city', 'temperature', 'humidity', 'condition', 'created_at')
    list_filter = ('city', 'created_at')
    ordering = ('-created_at',)
