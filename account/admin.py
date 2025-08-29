from django.contrib import admin
from .models import Image
# Register your models here.

# admin.site.register(Image)
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'user_id', 'date']
    # Можно добавить фильтры, поиск и т.д.
    list_filter = ['date', 'user']
    search_fields = ['title', 'description']