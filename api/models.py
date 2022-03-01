from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# making the the url_owner field a many to many field will enable several users own the samr url, right now that is not the case
class Url(models.Model):

    url_owner = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True)

    long_url = models.CharField(max_length=255, unique=True)
    short_url = models.CharField(max_length=255, unique=True)
    visits = models.PositiveBigIntegerField(default = 0)

    last_visit_time = models.DateField( null = True )
    created_time = models.DateField(auto_now=True)
