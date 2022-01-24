from django.db import models

class User(models.Model):
    _id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)


class Exercise(models.Model):
    id_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Exercises')
    description = models.CharField(max_length=100)
    duration = models.IntegerField(default=1)
    date_exercise = models.DateField()
