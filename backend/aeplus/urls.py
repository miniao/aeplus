"""aeplus URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'^api/partner/', include('partner.urls')),
    url(r'^api/blog/', include('blog.urls')),
    url(r'^api/subscribe/', include('subscribe.urls')),
    url(r'^api/institute/', include('institute.urls')),
    url(r'^api/resource/', include('resource.urls')),
    url(r'^api/prolib/', include('prolib.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
