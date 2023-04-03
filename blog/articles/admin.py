from django.contrib import admin
from .models import Article,Section
# Register your models here.


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Section)