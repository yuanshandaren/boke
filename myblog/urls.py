"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^login/$', 'blog.views.loginUser', name='loginUser'),
    url(r'^logout/$', 'blog.views.logoutUser', name='logoutUser'),
    url(r'^register/$', 'blog.views.register', name='register'),
    url(r'^post/(?P<id>[0-9]+)/$', 'blog.views.post', name='post'),
    url(r'^post/(?P<id>[0-9]+)/deleteBlog/$', 'blog.views.deleteBlog', name='deleteBlog'),
    url(r'^post/(?P<id>[0-9]+)/editBlog/$', 'blog.views.editBlog', name='editBlog'),
    url(r'^personal/(?P<id>[0-9]+)/createBlog/$', 'blog.views.createBlog', name='createBlog'),
    url(r'^personal/(?P<id>[0-9]+)/$', 'blog.views.personal', name='personal'),

    url(r'^accounts/weixin/login/$', 'oauth.views.weixin_login', name='weixin_login'),
    url(r'^accounts/weixin/login/done/$', 'oauth.views.weixin_auth', name='weixin_login_done'),
#    url(r'^complete/(?P<id>[0-9]+)/$', 'oauth.views.complete', name='complete'),
]








