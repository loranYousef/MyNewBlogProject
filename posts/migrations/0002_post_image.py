# Generated by Django 4.1.7 on 2023-04-01 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=' ', upload_to='posts/'),
            preserve_default=False,
        ),
    ]