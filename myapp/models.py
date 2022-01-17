from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse


# Bosh kategoriya
class  Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug':self.slug})


#pastda chiqib turadigon teglar jamlanmasi
class  Teg(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='links')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug':self.slug})

class Block(models.Model):
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    aftor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    view = models.IntegerField(default=1)
    category = models.ForeignKey( Category, on_delete=models.PROTECT)
    tag = models.ManyToManyField(Teg, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']