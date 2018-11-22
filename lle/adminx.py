import xadmin
from xadmin import views
from lle.models import *


# Register your models here.
class TypeAdmin:
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    list_filter = ['id', 'name']
    ordering = ['id']





class ContentAdmin:
    list_display = ["id",  "title", "picture",'publish']
    search_fields = ["id", "title", "picture"]



class CommentAdmin:
    # 在admin中显⽰顺序
    list_display = ["id",  "user_id", "news_id"]
    # 给admin添加搜索功能
    search_fields = ["id", "user_id", "news_id"]
    # 直接编辑字段
    # 排序字段

class BaseStting:
    enable_themes=True
    use_bootswatch=True

class GlobalSetting:
    site_title='朱老大后台管理系统'
    site_footer='扒鸡的新闻网站'
    menu_style='accordion'

xadmin.site.register(views.CommAdminView,GlobalSetting)
xadmin.site.register(views.BaseAdminView,BaseStting)
xadmin.site.register(Type, TypeAdmin)
xadmin.site.register(Content, ContentAdmin)
xadmin.site.register(Comment, CommentAdmin)
