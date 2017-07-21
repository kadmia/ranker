from django import template

from ..models import RankParent, Genre

register = template.Library()

@register.inclusion_tag('rank/rank_navbar.html')
def navbar():
    # TODO cache this so it doesn't hit the db all the time (perhaps just turn on django caching
    active_parents = RankParent.objects.filter(show_in_navbar=True, active=True)
    genres = Genre.objects.filter(active=True)
    return {'navbar_items': active_parents, 'genres': genres}