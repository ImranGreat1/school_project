# Generated by Django 2.2.1 on 2019-07-03 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190626_2024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_created']},
        ),
    ]
