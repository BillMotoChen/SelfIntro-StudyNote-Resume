from django.db import models

# Create your models here.

class Career(models.Model):
    title = models.CharField(max_length=200)
    date_start = models.DateField()
    date_end = models.DateField()
    event = models.CharField(max_length=100)
    event_description = models.TextField()
    note = models.TextField()
    on_going = models.BooleanField(default=False)

    def __str__(self):
        return self.title

