from django.conf import settings
from django.db import models


class Sample(models.Model):
    "Generated Model"
    user_id = models.BigIntegerField()
