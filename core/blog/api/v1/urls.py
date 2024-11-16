from django.urls import path
from .views import ApiPostList, ApiPostDetail

app_name = "api-v1"


urlpatterns = [
    # path("posts/", PostList.as_view(), name="api-post"),
    path("posts/", ApiPostList.as_view(), name="api-post"),
    path("posts/<int:pk>/", ApiPostDetail.as_view(), name="api-post-detail")
]
