from django import template
from myapp.models import Block, Teg




register = template.Library()


@register.inclusion_tag('popular_tpl.html')
def show_popular(son=3):
    trying = Block.objects.order_by('-view')[:son]
    return {'blocks': trying }

@register.inclusion_tag('tag_tpl.html')
def show_tag(son=3):
    trying = Teg.objects.all()
    return {'tags': trying }




    