from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class CommonModel(models.Model):
    class Meta:
        abstract = True

    internal_creation_datetime = models.DateTimeField(auto_now_add=True)
    internal_last_modified_datetime = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)


class CommonRankModel(CommonModel):
    class Meta:
        abstract = True

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    description = models.TextField()
    active = models.BooleanField(default=True)



class RankParent(CommonRankModel):
    show_in_navbar = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('rank:parent_index', args=[self.slug])

    def __unicode__(self):
        return u'%s' % (self.name)

    def __str__(self):
        return u'%s' % (self.name)


class GameState(CommonRankModel):
    def __unicode__(self):
        return u'%s' % (self.name)

    def __str__(self):
        return u'%s' % (self.name)


class Genre(CommonRankModel):
    def get_absolute_url(self):
        return reverse('rank:genre', args=[self.slug])

    def __unicode__(self):
        return u'%s' % (self.name)

    def __str__(self):
        return u'%s' % (self.name)


class Author(CommonRankModel):
    website = models.URLField(max_length=200, blank=True, null=True)
    def __unicode__(self):
        return u'%s' % (self.name)

    def __str__(self):
        return u'%s' % (self.name)



class RankEntity(CommonRankModel):
    parent = models.ForeignKey(RankParent, on_delete=models.CASCADE)
    votes = models.BigIntegerField(default=0)
    voter = models.ManyToManyField(User, blank=True)
    created = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    game_state = models.ForeignKey(GameState, on_delete=models.SET_NULL, null=True, blank=True)
    genre = models.ManyToManyField(Genre, blank=True, related_name='entities')
    authors = models.ManyToManyField(Author, blank=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    source_url = models.URLField(max_length=200, blank=True, null=True)
    documentation_url = models.URLField(max_length=200, blank=True, null=True)
    license_type = models.CharField(max_length=200, blank=True)


    def get_absolute_url(self):
        return reverse('rank:entity_index', args=[self.parent.slug, self.slug])

    def __unicode__(self):
        return u'%s:%s' % (self.parent.name, self.name)

    def __str__(self):
        return u'%s:%s' % (self.parent.name, self.name)


