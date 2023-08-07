from django import template

register = template.Library()

@register.filter
def has_expressed_interest(post, user):
    return post.interested_users.filter(id=user.id).exists()
