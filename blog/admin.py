from django.contrib import admin
from .models import Post, MoreImages, MorePdfs, MoreVideos, Comment, Pdf_File


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'date_created', 'last_updated')
    list_editable = ('status',)
    list_filter = ('status', 'date_created', 'last_updated')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(MoreImages)
admin.site.register(MorePdfs)
admin.site.register(MoreVideos)
admin.site.register(Comment)
admin.site.register(Pdf_File)
