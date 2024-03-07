from django.contrib import admin
from .models import Category, Post
# Register your models here.


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #Campos que se muestran en la lista
    list_display = ('title', 'author', 'published','post_categories')
    #, 'post_categories'
    #Si se desar ordenar solo por un campo se debe de ingresar : ordering = ('author', )
    ordering = ('author', 'published')
    search_fields = ('title','content','author__username','categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
