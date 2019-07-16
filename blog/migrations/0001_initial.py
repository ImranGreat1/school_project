# Generated by Django 2.2.1 on 2019-06-11 04:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='Post Images')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='Post PDFs')),
                ('video', models.FileField(blank=True, null=True, upload_to='Post Videos')),
                ('slug', models.SlugField(max_length=150)),
                ('audience', models.CharField(choices=[('departmental', 'Departmental'), ('faculty_wide', 'Faculty_wide'), ('school_wide', 'School_wide')], default='departmental', max_length=150)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish')], default='draft', max_length=10)),
                ('department', models.CharField(choices=[('computer science', 'Computer Science'), ('mathematics', 'Mathematics')], max_length=150)),
                ('level', models.CharField(choices=[('100', '100'), ('200', '200'), ('300', '300')], max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MoreVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='MoreVideos')),
                ('description', models.TextField(blank=True, max_length=150, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
        migrations.CreateModel(
            name='MorePdfs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='MorePDFs')),
                ('description', models.TextField(blank=True, max_length=150, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
        migrations.CreateModel(
            name='MoreImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='MoreImages')),
                ('description', models.TextField(blank=True, max_length=150, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=150)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
