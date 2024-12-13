"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap


sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', include("users.urls")),
    path('', include("website.urls")),
    path('blog/', include("blog.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps},
         name="django.contrib.sitemaps.views.sitemap"),
    path('robots.txt', include('robots.urls')),
    path('captcha/', include('captcha.urls')),
    path('zarinpal/', include('zarinpal.urls')),

]

handler404 = 'blog.views.error_404_view'
# handler500 = 'blog.views.page_not_found'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
