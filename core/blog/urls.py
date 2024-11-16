from django.urls import path, include
from .views import PostListView, PostDetailView, category, search_view


app_name = "blog"

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('single/<int:pk>/', PostDetailView.as_view(), name="blog-single"),
    path('category/<str:cat_name>/', category, name="blog-category"),
    path("search/", search_view, name="blog-search"),
    path("api/v1/", include("blog.api.v1.urls", namespace="v1")),
]
