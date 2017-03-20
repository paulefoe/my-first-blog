from django import template
from ..models import Post, published
from django.db.models import Count
from django.utils.safestring import mark_safe
# import markdown

register = template.Library()


@register.simple_tag
def total_posts():
    return published.count()


@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = published.order_by('-published_date')[:count]
    return {'latest_posts': latest_posts}


@register.assignment_tag
def get_most_commented_posts(count=5):
    return published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
