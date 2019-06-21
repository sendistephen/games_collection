from django.db import models

# Create your models here.

# game category


class GameCategory(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, default='')
    release_date = models.DateTimeField()
    game_category = models.CharField(max_length=200, blank=True, default='')
    played = models.BooleanField(default=False)
    game_category = models.ForeignKey(
        GameCategory, related_name='games', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Player(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (MALE, 'Male'), (FEMALE, 'Female'),
    created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=False, default='')
    gender = models.CharField(
        max_length=2, choices=GENDER_CHOICES, default=MALE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class PlayerScore(models.Model):
    player = models.ForeignKey(
        Player, related_name='scores', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField()
    score_date = models.DateTimeField()

    class Meta:
        # oreder by score descending
        ordering = ('-score',)
