from django.db import models

# Create your models here.
class Pieces(models.Model):
    composer = models.CharField(max_length=100)
    tonality = models.CharField(max_length=50)
    piece_name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    difficulty = models.IntegerField(default=0)
    master_level = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.piece_name

