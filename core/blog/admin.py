from django.contrib import admin
from blog.models import Post, Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('title', 'author', 'status', 'created_at', 'updated_at')
    empty_value_display = "EMPTY"
    list_filter = ('status', 'author')
    search_fields = ('titles',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("name",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
