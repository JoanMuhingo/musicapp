from django.db import models

# Create your models here.
class artiste(models.Model):
    first_name=models.TextField()
    last_name=models.TextField()
    age=models.TextField()

class song(models.Model):
    title=models.TextField()
    datereleased=models.TextField()
    likes=models.TextField()
    artiste_id=models.ForeignKey(artiste)

class lyric(models.Model):
    content=models.TextField()
    song_id=models.ForeignKey(song)    

   

 


