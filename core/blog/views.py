from typing import Any, Optional
from django.db import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Category, Post
from django.shortcuts import render
# Create your views here.


class PostListView(ListView):
    paginate_by = 6
    queryset = Post.objects.filter(status=1)
    template_name = "blog/home.html"
    ordering = "-created_at"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["posts"] = Post.objects.filter(status=1)
        context_data["categories"] = Category.objects.all()
        return context_data


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/blog-single.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["posts"] = Post.objects.filter(status=1)
        context_data["categories"] = Category.objects.all()
        return context_data


def error_404_view(request, exception):
    return render(request, "error-handling/error-404.html")


def category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {"page_obj": posts}
    return render(request, "blog/blog-filter.html", context)


def search_view(request):
    posts = Post.objects.filter(status=1)
    if request.method == "GET":
        if s := request.GET.get("s"):
            posts = posts.filter(content__contains=s)
        # try:
        #     print("TRY")
        #     page_number = request.GET.get('page')
        #     posts = posts.get_page(page_number)
        # except PageNotAnInteger:
        #     print("NOT INT")
        #     posts.get_page(1)
        # except EmptyPage:
        #     print("EMPTY")
        #     posts.get_page(1)

    context = {"page_obj": posts}
    return render(request, "blog/blog-filter.html", context)
