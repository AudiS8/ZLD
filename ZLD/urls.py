"""ZLD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf import settings
from django.views.static import serve
from django.conf.urls import include
from lle import views
import xadmin
from lle.views import *

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^$',views.Index),
    url(r'^$', views.Index, name='index'),
    url(r'^login$', Login.as_view(), name='login'),
    url(r'^logout$', Logout.as_view(), name='logout'),
    url(r'^signup$', Signup.as_view(), name='signup'),
    url(r"^news/(?P<content_id>\d+)", NewsView.as_view()),
    url(r'captcha/', include('captcha.urls')),
    url(r"^setuser/(?P<user_id>\d+)", SetUserView.as_view()),
    url(r"^password_reset/(?P<user_id>\d+)$", password_reset),
    url(r"^forgetpwd$", ForGetPassword.as_view()),
    url(r"^getyzm/(?P<user_id>\d+)/(?P<code>\w+)", getyzm)
]
