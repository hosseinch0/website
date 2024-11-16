from django.views.generic import ListView, CreateView
from .forms import NewsLetterForm, ContactForm
from django.shortcuts import render, redirect
from django.forms.models import BaseModelForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from blog.models import Post
from .models import Contact
# Create your views here.


class HomePostsListView(ListView):

    queryset = Post.objects.filter(status=1).order_by("-published_at")[:3]
    paginate_by = 3
    template_name = "website/index.html"


# class WebsiteContactView(CreateView):

#     model = Contact
#     form_class = ContactForm
#     template_name = "website/contact.html"
#     success_url = "/contact/"

#     def form_valid(self, form):
#         form = self.get_form()
#         if form.is_valid():
#             self.object = form.save()
#         else:
#             pass
#         return super().form_valid(form)


def about_view(request):
    return render(request, "website/about-us.html")


def newsletter_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = NewsLetterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("../")
        return redirect("../")


def contact_message(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(
                    request, messages.SUCCESS, "Message sent successfully")
                return HttpResponseRedirect(reverse("website:contact"))
            else:
                messages.add_message(
                    request, messages.ERROR, "Something went wrong make sure Captcha is validate")
                return HttpResponseRedirect(reverse("website:contact"))
        form = ContactForm()
        return render(request, "website/contact.html", {"form": form})
