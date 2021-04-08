from django.db import models

class Novel(models.Model):
    title = models.SlugField(max_length=180, null=False)
    alter_title = models.CharField(max_length=180, null=True, blank=True)
    description = models.TextField(max_length=666, null=True, blank=True)
    date_emission = models.DateTimeField(null=True, blank=True)
    cover_path = models.CharField(max_length=255, null=True, blank=True)

    TYPE_CHOICES = [
        ('LN', 'Light novel'),
        ('WN', 'Web novel')
    ]
    type = models.CharField(max_length=2, null=False, choices=TYPE_CHOICES ,default=TYPE_CHOICES[0][0])

    STRUCTURE_CHOICES = [
        ('VOL', 'Volumes'),
        ('CHA', 'Chapters')
    ]
    structure = models.CharField(max_length=3, null=False, choices=STRUCTURE_CHOICES, default=[0][0])

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    n_likes = models.IntegerField(editable=False)
    n_dislikes = models.IntegerField(editable=False)
    n_views = models.IntegerField(editable=False)