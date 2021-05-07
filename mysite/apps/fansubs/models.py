from django.db import models
    
class Fansub(models.Model):
    name           = models.CharField(max_length=120, null=False, blank=False, unique=True)
    about          = models.TextField(max_length=666, null=True, blank=True)
    cover          = models.ImageField(upload_to='fansubs/', max_length=100, null=True, blank=True)
    external       = models.JSONField(null=True, blank=True)
    creation_date  = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    last_update    = models.DateTimeField(auto_now=True)
    likes          = models.IntegerField(editable=False, default=0)
    dislikes       = models.IntegerField(editable=False, default=0)
    views          = models.IntegerField(editable=False, default=0)
    
    contribs       = models.ManyToManyField('novels.Chapter', through='Contrib', through_fields=('fansub', 'chapter') )
    members        = models.ManyToManyField('users.User', through='Membership', through_fields=('fansub', 'user') )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = 'Fansub'
        verbose_name_plural = 'Fansubs'


class Contrib(models.Model):
    fansub        = models.ForeignKey('Fansub', on_delete=models.CASCADE, null=False, blank=False, related_name='contrib_fansub')
    chapter       = models.ForeignKey('novels.Chapter', on_delete=models.CASCADE, null=False, blank=False, related_name='chapter_fansub')

    content       = models.TextField(null=False, blank='False')

    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    last_update   = models.DateTimeField(auto_now=True)
    views         = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return '{0} - {1}'.format(self.fansub.name, self.chapter.distro.title)

    class Meta:
        verbose_name        = 'Contribución'
        verbose_name_plural = 'Contribuciones'


class Membership(models.Model):
    fansub      = models.ForeignKey('Fansub', on_delete=models.CASCADE, null=False, blank=False, related_name='member_fansub')
    user        = models.ForeignKey('users.User', on_delete=models.CASCADE, null=False, blank=False, related_name='member_user')

    ROLE_CHOICES = [
        ('LE', 'Leader'),
        ('ME', 'Member'),
        ('TR', 'Traductor'),
        ('AR', 'Artist'),
        ('ED', 'Editor'),
        ('UP', 'Uploader')
    ]

    role        = models.CharField(max_length=2, null=True, choices=ROLE_CHOICES, default=ROLE_CHOICES[1][0], verbose_name='Rol')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de unión')

    def __str__(self):
        return '{0} - {1}'.format(self.fansub.name, self.user.username)

    class Meta:
        verbose_name        = 'Miembro'
        verbose_name_plural = 'Miembros'