from django.db import models
from datetime import date

class Chat(models.Model):
    user_name = models.CharField(max_length=30)
    message = models.TextField()
    date = models.DateField(default=date.today)


