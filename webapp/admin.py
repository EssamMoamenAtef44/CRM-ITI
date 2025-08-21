from django.contrib import admin
from .models import Category, Record

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass