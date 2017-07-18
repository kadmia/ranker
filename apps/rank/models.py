from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class CommonModel(models.Model):
    class Meta:
        abstract = True

    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_modified_datetime = models.DateTimeField(auto_now=True)
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


class RankEntity(CommonRankModel):
    parent = models.ForeignKey(RankParent, on_delete=models.CASCADE)
    votes = models.BigIntegerField(default=0)
    voter = models.ManyToManyField(User, blank=True)

    def get_absolute_url(self):
        return reverse('rank:entity_index', args=[self.parent.slug, self.slug])

    def __unicode__(self):
        return u'%s:%s' % (self.parent.name, self.name)

    def __str__(self):
        return u'%s:%s' % (self.parent.name, self.name)
