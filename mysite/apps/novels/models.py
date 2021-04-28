from django.db import models
from multiselectfield import MultiSelectField

class Novel(models.Model):
    title         = models.CharField(max_length=180, null=False, blank=False)
    alter_title   = models.CharField(max_length=180, null=True, blank=True)
    description   = models.TextField(max_length=666, null=True, blank=True)
    date_emission = models.DateField(null=True, blank=True)
    cover_path    = models.SlugField(max_length=255, null=True, blank=True)

    TYPE_CHOICES = [
        ('LN', 'Light novel'),  
        ('WN', 'Web novel')
    ]
    STRUCTURE_CHOICES = [
        ('VOL', 'Volumes'),
        ('ARC', 'Arcs'),
        ('CHA', 'Chapters')
    ]

    type          = models.CharField(max_length=2, null=False, choices=TYPE_CHOICES ,default=TYPE_CHOICES[0][0], verbose_name='Tipo')
    structure     = models.CharField(max_length=3, null=False, choices=STRUCTURE_CHOICES, default=STRUCTURE_CHOICES[0][0], verbose_name='Estructura')

    GENRE_CHOICES = [
        ('---', ''),
        ('ATN', 'Action'),
        ('ADV', 'Adventure'),
        ('CLB', 'Celebrity'),
        ('CMD', 'Comedy'),
        ('DRM', 'Drama'),
        ('ECC', 'Ecchi'),
        ('FNT', 'Fantasy'),
        ('GNB', 'Gender Blender'),
        ('HRM', 'Harem'),
        ('HIS', 'Historical'),
        ('HOR', 'Horror'),
        ('JOS', 'Josei'),
        ('MLA', 'Martial Arts'),
        ('MTE', 'Mature'),
        ('MCA', 'Mecha'),
        ('MYS', 'Mystery'),
        ('PSY', 'Psychological'),
        ('ROM', 'Romance'),
        ('SCL', 'School Life'),
        ('SFI', 'Sci-fi'),
        ('SEI', 'Seinen'),
        ('STA', 'Shotacon'),
        ('SHO', 'Shoujo'),
        ('SAI', 'Shoujo Ai'),
        ('SOL', 'Slife of Life'),
        ('SOS', 'Sports'),
        ('SUP', 'Supernatural'),
        ('TRA', 'Tragedy'),
        ('WUX', 'Wuxia'),
        ('YAO', 'Yaoi'),
        ('YUI', 'Yuri'),
    ]

    genre         = MultiSelectField(choices=GENRE_CHOICES, max_length=3, default=GENRE_CHOICES[0][0])

    author        = models.JSONField(null=True)
    artist        = models.JSONField(null=True)

    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    last_update   = models.DateTimeField(auto_now=True)
    likes         = models.IntegerField(editable=False, default=0, verbose_name='Likes')
    dislikes      = models.IntegerField(editable=False, default=0, verbose_name='Dislikes')
    views         = models.IntegerField(editable=False, default=0, verbose_name='Vistas')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name        = 'Novela'
        verbose_name_plural = 'Novelas'


class Distro(models.Model):
    title         = models.CharField(max_length=180, null=False, blank=False)
    numero        = models.SmallIntegerField(verbose_name='Volumen número')
    description   = models.TextField(max_length=666, null=True, blank=True)
    cover_path    = models.SlugField(max_length=255, null=True, blank=True)
    emision_date  = models.DateField(verbose_name='Fecha de emisión', null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    last_update   = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    novel         = models.ForeignKey('Novel', on_delete=models.CASCADE, null=False, blank=False, related_name='distro_novel', verbose_name='Novela')
    likes         = models.IntegerField(editable=False, default=0)
    dislikes      = models.IntegerField(editable=False, default=0)
    views         = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name        = 'Distribución'
        verbose_name_plural = 'Distribuciones'


class Chapter(models.Model):
    title         = models.CharField(max_length=180, null=True, blank=True)
    numero        = models.SmallIntegerField()
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    last_update   = models.DateTimeField(auto_now=True)
    new_content   = models.BooleanField()

    TYPE_CHOICES = [
        ('PRO', 'Prologue'),
        ('EPI', 'Epilogue'),
        ('INT', 'Intermediate'),
        ('NOR', 'Normal'),
        ('ATW', 'Autor words'),
        ('SPE', 'Special')
    ]

    type          = models.CharField(max_length=3, null=True, choices=TYPE_CHOICES, default=TYPE_CHOICES[3][0], verbose_name='Tipo')
    distro        = models.ForeignKey('Distro', on_delete=models.CASCADE, null=False, blank=False, related_name='chapter_distro', verbose_name='Distribución')
    views         = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return 'Capítulo {0}'.format(self.numero)

    class Meta:
        verbose_name        = 'Capítulo'
        verbose_name_plural = 'Capítulos'


def distro_directory_path(instance, filename):
    return 'novels/{0}/{1}/{2}'.format(instance.distro.novel.id, instance.distro.id, filename)

class Illustration(models.Model):
    name        = models.SlugField(max_length=60, null=True, blank=True)
    picture     = models.ImageField(upload_to=distro_directory_path, max_length=100, null=False)
    distro      = models.ForeignKey('Distro', on_delete=models.CASCADE, null=False, blank=False, related_name='illustration_distro', verbose_name='Distribución')
    uploaded_by = models.ForeignKey('users.User', on_delete=models.CASCADE, null=False, blank=False, related_name='illustration_user', verbose_name='Usuario')
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de subida')

    def __str__(self):
        return self.name if self.name else self.picture

    class Meta:
        verbose_name        = 'Ilustración'
        verbose_name_plural = 'Ilustraciones'