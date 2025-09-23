from django.db import models

class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
    def get_date(self):
        return self.date_created.strftime('%b %d, %Y')

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def song_count(self):
        return self.song_set.count()

class Song(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    artiste = models.ForeignKey(Artiste, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    song = models.OneToOneField(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"Lyric for {self.song.title}"
