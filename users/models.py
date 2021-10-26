from django.db   import models

from core.models import TimeStampModel

class User(TimeStampModel):
    name     = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    email    = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'users'