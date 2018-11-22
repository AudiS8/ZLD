from django.contrib import admin
from lle.models import *


# Register your models here.
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    list_filter = ['id', 'name']
    ordering = ['id']


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["username", "gender", "mobile", "email", "is_staff", "is_superuser"]
    search_fields = ["username", "gender", "mobile", "email"]
    list_filter = ["username", "gender", "mobile", "email"]
    list_editable = ["is_staff", "is_superuser"]
    ordering = ["id"]


class ContentAdmin(admin.ModelAdmin):
    list_display = ["id",  "title", "picture"]
    search_fields = ["id", "title", "picture"]



class CommentAdmin(admin.ModelAdmin):
    # 在admin中显⽰顺序
    list_display = ["id",  "user_id", "news_id"]
    # 给admin添加搜索功能
    search_fields = ["id", "user_id", "news_id"]
    # 直接编辑字段
    # 排序字段



admin.site.register(Type, TypeAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Comment, CommentAdmin)
