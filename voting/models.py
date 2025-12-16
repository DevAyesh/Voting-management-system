from django.db import models

class Vote(models.Model):
    preferences = models.TextField() # Encrypted string


    class Meta:
        db_table = 'vote'
