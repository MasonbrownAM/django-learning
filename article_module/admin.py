from django.contrib import admin
from .models import Article,ArticleCathegory
# Register your models here.
class ArticleCathegoryAdmin(admin.ModelAdmin):
    list_display_links = ['title']
    list_display = ['title', 'parent']
    list_editable = ['parent']

class ArticleAdmin(admin.ModelAdmin):
    list_display_links = ['title']
    list_display = ['title','is_active', 'slug', 'author']
    list_editable = ['is_active']
    def save_model(self, request, obj:Article, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCathegory, ArticleCathegoryAdmin)