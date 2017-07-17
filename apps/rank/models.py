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


class RankEntity(CommonModel):
    parent = models.ForeignKey(RankParent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    description = models.TextField()
    votes = models.BigIntegerField()
    voter = models.ManyToManyField(User, blank=True)

