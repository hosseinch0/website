from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "monthly"

    def items(self):
        return ["website:home", "website:contact", "website:about"]

    def location(self, item):
        return reverse(item)
