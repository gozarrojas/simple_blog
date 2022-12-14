from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from categories.models import Category
from django.urls import reverse


class Post(models.Model):
    # ForeignKey - 1 a M
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Nombre de Usuario')
    profile = models.ForeignKey('users.Profile', on_delete=models.PROTECT)
    title = models.CharField(max_length=255, unique=True, verbose_name='Titulo')
    image_header = models.ImageField(upload_to='posts/photos', verbose_name='Imagen', blank=True)
    post = RichTextField
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # ¿Es un borrador?
    is_draft = models.BooleanField(default=True)
    url = models.SlugField(max_length=255, unique=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    # muchos a muchos
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return '{} by @{}'.format(self.title, self.user.username)

    #Se requiere cuando se utiliza CreateView
    # def get_absolute_url(self):
    #     return reverse('posts:detail', args=(str(self.url)))

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
