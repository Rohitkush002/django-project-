from django.db import models

class NewUsers(models.Model):
    username=models.CharField(max_length=50, unique=True)
    password=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mobile=models.CharField(max_length=15)
    status=models.CharField(max_length=10, default='Active')

    def __str__(self):
        return self.username


