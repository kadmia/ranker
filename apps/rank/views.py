from django.shortcuts import render, get_object_or_404
from apps.rank.models import RankParent, RankEntity


def index(request):
    parents = RankParent.objects.all()
    context = {'rank_parents': parents}
    return render(request, 'rank/rank_parents.html', context)


def parent_index(request, parent_slug):
    print('Parent: ' + parent_slug)
    entities = RankEntity.objects.filter(parent__slug=parent_slug)
    context = {'rank_entities': entities}
    return render(request, 'rank/rank_parent.html', context)


def entity_index(request, parent_slug, entity_slug):
    print('Entity: ' + entity_slug)
    entity = RankEntity.objects.filter(parent__slug=parent_slug, slug=entity_slug)
    e = get_object_or_404(entity)
    context = {'entity': e}
    return render(request, 'rank/rank_entity.html', context)
