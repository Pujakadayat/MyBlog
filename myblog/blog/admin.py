from django.contrib import admin

from .models import *


# Register your models here.


# FOR CONFIGURATION OF CATEGORY ADMIN
# admin option enable garna yesko class ko yesko parent banako
class CategoryAdmin(admin.ModelAdmin):
    # kun kun property admin table  jasari dekhauna tyo list ma lekhne
    list_display = ('image_tag','title','description', 'urls','add_date')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50

class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'name', 'email', 'message', 'is_approved','date')


    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/7/tinymce.min.j','js/script.js',)

# CUSTOMADMIN CATEGORY PASS GARE Category TA HAMRO MAIN MODEL VAYO TARA HAMILE SUTOMADMIN MODEL BANAKO XAU TESLAI BADI PREFERENCE MILXA
admin.site.register(Category,CategoryAdmin)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)