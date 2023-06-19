from django.contrib import admin
from post_app.models import Post,Like

# Register your models here.

class PostAdmin(admin.ModelAdmin):
       list_display=('post_text', 'created_at','like')
admin.site.register(Post , PostAdmin)

class LikeAdmin(admin.ModelAdmin):
       list_display=('is_active', 'created_at',)
admin.site.register(Like , LikeAdmin)

