# Generated by Django 2.2.1 on 2019-07-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190713_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='end',
            field=models.DurationField(null=True, verbose_name='Ending at'),
        ),
        migrations.AddField(
            model_name='course',
            name='start',
            field=models.DurationField(null=True, verbose_name='Starting at'),
        ),
        migrations.DeleteModel(
            name='Time',
        ),
    ]
