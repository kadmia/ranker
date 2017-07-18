from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CommonModel(models.Model):
    class Meta:
        abstract = True

    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_modified_datetime = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)


class RankParent(CommonModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    description = models.TextField()
    active = models.BooleanField(default=True)
    show_in_navbar = models.BooleanField(default=False)
    

    def __unicode__(self):
        return u'%s' % (self.name)

    def __str__(self):
        return u'%s' % (self.name)


class RankEntity(CommonModel):
    parent = models.ForeignKey(RankParent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    description = models.TextField()
    votes = models.BigIntegerField(default=0)
    voter = models.ManyToManyField(User, blank=True)

    def __unicode__(self):
        return u'%s:%s' % (self.parent.name, self.name)

    def __str__(self):
        return u'%s:%s' % (self.parent.name, self.name)
