from django import template
from blog.models import Post, Category

register = template.Library()


@register.inclusion_tag('blog/latest-posts.html')
def latest_posts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_at')[:arg]
    return {"posts": posts}


@register.inclusion_tag('blog/cat.html')
def all_categories():
    categories = Category.objects.all()
    return {"categories": categories}


@register.inclusion_tag("blog/previous-post.html")
def pre_post_exist(postId, **kwargs):
    posts = Post.objects.all()
    ''' THIS FUNCTION MAKES SURE ABOUT THE PREVIOUS POST EXISTENCE AND ASSIGN THEIR POST ID'S SO THE USER CAN MOVE BETWEEN THEM '''
    for turn in range(1, postId):
        prevPosts = Post.objects.filter(status=1, pk=postId - turn)
        if not len(prevPosts) == 0:
            return {"prevPosts": prevPosts}
        else:
            continue


@register.inclusion_tag("blog/next-post.html")
def next_post_exist(postId, **kwargs):
    posts = Post.objects.all()
    ''' THIS FUNCTION MAKES SURE ABOUT THE NEXT POST EXISTENCE AND ASSIGN THEIR POST ID'S SO THE USER CAN MOVE BETWEEN THEM '''
    for turn in range(1, posts.count()):
        nextPosts = Post.objects.filter(status=1, pk=postId + turn)
        if not len(nextPosts) == 0:
            print(nextPosts)
            return {"nextPosts": nextPosts}
        else:
            continue
