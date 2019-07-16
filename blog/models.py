from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms


# Custom QuerySet -> allows you to use post.objects.all().published
class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status='publish')


# Custom Model Manager -> allows you to use post.objects.published
class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().filter(status='publish')






class Post(models.Model):
    from .info import department_choice, level_choice, status_choice, audience_choice

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to='Post_Images', blank=True, null=True)
    pdf = models.FileField(upload_to='Post_PDFs', blank=True, null=True)
    video = models.FileField(upload_to='Post_Videos', blank=True, null=True)
    slug = models.SlugField(max_length=150)
    audience = models.CharField(max_length=150, choices=audience_choice, default='departmental')
    date_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    last_updated = models.DateTimeField(verbose_name="Date Updated", auto_now=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    status = models.CharField(max_length=10, choices=status_choice, default='draft')
    department = models.CharField(max_length=150, choices=department_choice)
    level = models.CharField(max_length=10, choices=level_choice)
    favourite = models.ManyToManyField(User, related_name='favourites', blank=True)
    restrict_comment = models.BooleanField(default=False)


    objects = PostManager()

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    def total_likes(self):
        return self.likes.count()
    


class MoreImages(models.Model):
    from .info import department_choice, level_choice, status_choice

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='MoreImages')
    description = models.TextField(max_length=150, blank=True, null=True)
    department = models.CharField(max_length=150, choices=department_choice)
    level = models.CharField(max_length=150, choices=level_choice)
    status = models.CharField(max_length=150, choices=status_choice)

    def __str__(self):
        return f'{self.post}, Images'


class MorePdfs(models.Model):
    from .info import department_choice, level_choice, status_choice

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='MorePDFs')
    description = models.TextField(max_length=150, blank=True, null=True)
    department = models.CharField(max_length=150, choices=department_choice)
    level = models.CharField(max_length=150, choices=level_choice)
    status = models.CharField(max_length=150, choices=status_choice)

    def __str__(self):
        return f'"{self.post}" Pdf'


class MoreVideos(models.Model):
    from .info import department_choice, level_choice, status_choice

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    video = models.FileField(upload_to='MoreVideos')
    description = models.TextField(max_length=150, blank=True, null=True)
    department = models.CharField(max_length=150, choices=department_choice)
    level = models.CharField(max_length=150, choices=level_choice)
    status = models.CharField(max_length=150, choices=status_choice)

    def __str__(self):
        return f'"{self.post}" Videos'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=150)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.title} "comment"- by {self.user.username}'

    class Meta:
        ordering = ('-timestamp',)



# class ImageAlbum(models.Model):
#     posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     images = models.ManyToManyField(ImageAlbum, related_name='images')
#     album_name = models.CharField(max_length=150)



# class Images(models.Model):
#     image1 = models.ImageField(upload_to='Album Images')
#     image2 = models.ImageField(upload_to='Album Images')
#     image3 = models.ImageField(upload_to='Album Images')
#     description = models.TextField()


class Pdf_File(models.Model):
    from .info import department_choice, level_choice

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='pdf_files')
    title = models.CharField(max_length=150)
    department = models.CharField(max_length=150, choices=department_choice)
    level = models.CharField(max_length=150, choices=level_choice)
    books = models.ManyToManyField(User, related_name='books', blank=True)
    is_mybook = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.title} pdf'


    def my_book(self):
        if self.is_mybook == True:
            return True
        return False




