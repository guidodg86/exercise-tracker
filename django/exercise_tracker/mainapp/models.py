import secrets
from django.db import models

class User(models.Model):
    _id = models.CharField(max_length=25, primary_key=True)
    username = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self._id:
            already_exists = True
            while already_exists:
                _id = secrets.token_hex(12)
                already_exists = User.objects.filter(pk=_id).exists()
            self._id = _id
        super(User, self).save(*args, **kwargs)

class Exercise(models.Model):
    id_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='log')
    description = models.CharField(max_length=100)
    duration = models.IntegerField(default=1)
    date_exercise = models.DateTimeField()
