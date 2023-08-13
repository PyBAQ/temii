from django.db import models

from temii.users.models import User


class TalkLanguage(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class TalkLevel(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Talk(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    level = models.ForeignKey(TalkLevel, on_delete=models.PROTECT)
    language = models.ForeignKey(TalkLanguage, on_delete=models.PROTECT)
    timezone = models.CharField(max_length=60)
    comments = models.CharField(max_length=300)
