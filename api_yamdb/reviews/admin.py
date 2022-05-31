from django.contrib import admin
from .models import Review, Comment

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'text', 'pub_date', 'score')
    empty_value_display = '-пусто-'
    search_fields = ('text',)
    list_filter = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'author', 'text', 'pub_date')
    empty_value_display = '-пусто-'
    search_fields = ('text',)
    list_filter = ('review',)


admin.site.register(Comment, CommentAdmin)
admin.site.register(Review, ReviewAdmin)
