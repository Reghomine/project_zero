from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Icecream(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    avatar = models.ImageField(blank=True, null=True)
    rating = models.IntegerField()




