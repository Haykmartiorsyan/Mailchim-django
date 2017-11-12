from django.db import models


class SignupFormPlugin(models.Model):
    list_id = models.CharField(max_length=30)

    def __str__(self):
        return self.list_id

    def __unicode__(self):
        return self.list_id