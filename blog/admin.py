from django.contrib import admin
from blog.models import Post
from django.contrib.auth.models import User
# Register your models here.
#class postAdmin(admin.ModelAdmin):
#    fields = ['Post_text', 'author']

#class UserAdmin(admin.ModelAdmin):
#    fields = ['name', 'email', 'website']
 #   search_fields = ('name',)

#admin.site.register(User, UserAdmin)
admin.site.register(Post)
