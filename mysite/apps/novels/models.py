from django.db import models

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
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    last_update   = models.DateTimeField(auto_now=True)
    n_likes       = models.IntegerField(editable=False, default=0, verbose_name='Likes')
    n_dislikes    = models.IntegerField(editable=False, default=0, verbose_name='Dislikes')
    n_views       = models.IntegerField(editable=False, default=0, verbose_name='Vistas')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name        = 'Novela'
        verbose_name_plural = 'Novelas'


class Volume(models.Model):
    title         = models.CharField(max_length=180, null=False, blank=False)
    number        = models.SmallIntegerField(verbose_name='nº')
    description   = models.TextField(max_length=666, null=True, blank=True)
    cover_path    = models.SlugField(max_length=255, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    last_update   = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    novel_id      = models.ForeignKey('Novel', on_delete=models.CASCADE, null=False, blank=False, related_name='volume_novel', verbose_name='Novela')
    n_likes       = models.IntegerField(editable=False, default=0, verbose_name='Likes')
    n_dislikes    = models.IntegerField(editable=False, default=0, verbose_name='Dislikes')
    n_views       = models.IntegerField(editable=False, default=0, verbose_name='Vistas')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name        = 'Volumen'
        verbose_name_plural = 'Volúmenes'


class Chapter(models.Model):
    title         = models.CharField(max_length=180, null=True, blank=True)
    number        = models.SmallIntegerField(verbose_name='nº')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    last_update   = models.DateTimeField(auto_now=True)

    TYPE_CHOICES = [
        ('PRO', 'Prologue'),
        ('EPI', 'Epilogue'),
        ('INT', 'Intermediate'),
        ('NOR', 'Normal'),
        ('ATW', 'Autor words'),
        ('SPE', 'Special')
    ]

    type          = models.CharField(max_length=3, null=True, choices=TYPE_CHOICES, default=TYPE_CHOICES[3][0], verbose_name='Tipo')
    volume_id     = models.ForeignKey('Volume', on_delete=models.CASCADE, null=False, blank=False, related_name='chapter_volume', verbose_name='Volumen')
    n_likes       = models.IntegerField(editable=False, default=0, verbose_name='Likes')
    n_dislikes    = models.IntegerField(editable=False, default=0, verbose_name='Dislikes')
    n_views       = models.IntegerField(editable=False, default=0, verbose_name='Vistas')

    def __str__(self):
        return 'Capítulo {0}'.format(self.number)

    class Meta:
        verbose_name        = 'Capítulo'
        verbose_name_plural = 'Capítulos'


# Subida de ilustraciones a novelas/id_novela/id_volumen/nombre_imagen.jpg*
# La instancia es el objeto actual y se mueve mediante las Foreign Keys
def volume_directory_path(instance, filename):
    return 'novels/{0}/{1}/{2}'.format(instance.volume_id.novel_id.id, instance.volume_id.id, filename)

# Surge la necesidad de eliminar la imagen anterior si es reemplazada (actualmente no lo hace, solucionar)
class Illustration(models.Model):
    name        = models.SlugField(max_length=60, null=True, blank=True)
    picture     = models.ImageField(upload_to=volume_directory_path, max_length=100, null=False)
    volume_id   = models.ForeignKey('Volume', on_delete=models.CASCADE, null=False, blank=False, related_name='illustration_volume', verbose_name='Volumen')
    uploaded_by = models.ForeignKey('users.User', on_delete=models.CASCADE, null=False, blank=False, related_name='illustration_user', verbose_name='Usuario')
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de subida')

    def __str__(self):
        return self.name if self.name else self.picture

    class Meta:
        verbose_name        = 'Ilustración'
        verbose_name_plural = 'Ilustraciones'