from django.contrib import admin
from .models import Contact, NewsLetter

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ["sender", "email", "created_at", "subject", "name"]
    search_fields = ["sender" ,"email", "name", ]
    list_filter = ["email"]
    ordering = ["created_at",]

    class Meta:
        model = Contact


admin.site.register(Contact, ContactAdmin)


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ["sender", "email", "created_at"]
    search_fields = ['sender', 'email']
    ordering = ["created_at"]
    list_filter = ["sender__is_active"]

    class Meta:
        model = NewsLetter


admin.site.register(NewsLetter, NewsLetterAdmin)
