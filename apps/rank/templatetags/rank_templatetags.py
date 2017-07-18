from django import template

from ..models import RankParent

register = template.Library()

@register.inclusion_tag('rank/rank_navbar.html')
def navbar():
    # TODO cache this so i don't hit the db all the time 
    active_parents = RankParent.objects.filter(show_in_navbar=True)
    return {'navbar_items': active_parents}