from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Post
from django.utils.text import slugify


@receiver(pre_save, sender=Post)
def slugify_title(sender, instance, **kwargs):
    title = instance.title
    slug_title = slugify(title)
    instance.slug = slug_title
