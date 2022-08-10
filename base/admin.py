from django.contrib import admin
from .models import Images, Post


class ImagesAdmin(admin.StackedInline):
    model = Images
 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImagesAdmin]
 
    class Meta:
       model = Post
 
@admin.register(Images)
class PostImageAdmin(admin.ModelAdmin):
    pass

