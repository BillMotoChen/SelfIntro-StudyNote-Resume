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

class Pieces(models.Model):
    # piece info
    piece_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    tonality = models.CharField(max_length=100)
    difficulty = models.PositiveIntegerField()

    '''
    0 - not yet but want to play
    1 - just started (on going)
    2 - memorized, trying to master
    3 - mastered
    '''
    status = models.PositiveIntegerField()
    link = models.CharField(max_length=300)  # youtube vid link
    description = models.TextField()
    first_page_img = models.CharField(max_length=200)

    note = models.TextField(default="Nothing Special")

    def __str__(self):
        return self.title

