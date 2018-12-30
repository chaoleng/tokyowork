from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.IntegerField(default=0)
    user_name = models.CharField(max_length=30)
    user_register_time  = models.DateTimeField('date published')
    user_place = models.CharField(max_length=50)


class Card(models.Model):
    card_id = models.IntegerField(default=0)
    card_update = models.DateTimeField('date published')
    card_time  = models.DateTimeField('date published')
    create_id = models.CharField(max_length=50)
    create_name = models.CharField(max_length=50)
    card_state = models.CharField(max_length=30)
    card_title = models.CharField(max_length=30)
    card_content = models.CharField(max_length=100)
		

