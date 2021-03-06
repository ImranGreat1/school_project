# Generated by Django 2.2.1 on 2019-06-26 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190626_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='morepdfs',
            name='department',
            field=models.CharField(choices=[('computer science', 'Computer Science'), ('mathematics', 'Mathematics')], default='computer science', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='morepdfs',
            name='level',
            field=models.CharField(choices=[('100', '100'), ('200', '200'), ('300', '300')], default='100', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='morepdfs',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish')], default='publish', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='morevideos',
            name='department',
            field=models.CharField(choices=[('computer science', 'Computer Science'), ('mathematics', 'Mathematics')], default='computer science', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='morevideos',
            name='level',
            field=models.CharField(choices=[('100', '100'), ('200', '200'), ('300', '300')], default='100', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='morevideos',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish')], default='publish', max_length=150),
            preserve_default=False,
        ),
    ]
