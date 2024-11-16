from django.urls import path
from .views import HomePostsListView, about_view, contact_message, newsletter_view


app_name = "website"


urlpatterns = [
    path("", HomePostsListView.as_view(), name="home"),
    path("about/", about_view, name="about"),
    path("contact/", contact_message, name="contact"),
    path("newsletter/", newsletter_view, name="newsletter"),
]
