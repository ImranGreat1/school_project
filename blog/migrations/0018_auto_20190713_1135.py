# Generated by Django 2.2.1 on 2019-07-13 11:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0017_auto_20190713_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf_file',
            name='books',
            field=models.ManyToManyField(related_name='books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='My_books',
        ),
    ]
