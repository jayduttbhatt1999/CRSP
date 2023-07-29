from django.contrib import admin
from keneel.models import register
from accounts.models import Profile ,Post, Connection, Skill, SavedPost, Comment, Notification, ResearchCollaborationPost
# Register your models here.

admin.site.register(register)
# admin.site.register(profiles)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Connection)
admin.site.register(Skill)
admin.site.register(SavedPost)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(ResearchCollaborationPost)

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'authors', 'keywords', 'abstract', 'paper', 'allow_downloading', 'published_on', 'uploaded_by')

# admin.site.register(Post, PostAdmin)