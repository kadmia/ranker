from django.shortcuts import render, get_object_or_404, redirect
from apps.rank.models import RankParent, RankEntity, Genre
from django.contrib import messages


def index(request):
    parents = RankParent.objects.all()
    context = {'rank_parents': parents}
    return render(request, 'rank/rank_parents.html', context)


def genre_index(request):
    genres = Genre.objects.filter(active=True)
    context = {'genres': genres}
    return render(request, 'rank/genre_index.html', context)


def genre(request, genre_slug):
    print('genre: ' + genre_slug)
    g = get_object_or_404(Genre, slug=genre_slug)
    context = {'genre': g}
    return render(request, 'rank/genre.html', context)


def parent_index(request, parent_slug):
    entities = RankEntity.objects.filter(parent__slug=parent_slug)
    context = {'rank_entities': entities}
    return render(request, 'rank/rank_parent.html', context)


def entity_index(request, parent_slug, entity_slug):
    entity = get_object_or_404(RankEntity, parent__slug=parent_slug, slug=entity_slug)
    context = {'entity': entity}
    return render(request, 'rank/rank_entity.html', context)


def vote(request, parent_slug, entity_slug):
    entity = get_object_or_404(RankEntity, parent__slug=parent_slug, slug=entity_slug)
    if entity.parent.active and entity.active:
        entity.votes += 1
        entity.save()
        messages.add_message(request, messages.INFO, 'Your vote has been saved')
    else:
        messages.add_message(request, messages.INFO, 'This ranking has been deactivated')
    return redirect(entity)
