from django.contrib import admin
from myapp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_submit')
    list_display_links = ('id', 'title_submit')


admin.site.register(Article, ArticleAdmin)
