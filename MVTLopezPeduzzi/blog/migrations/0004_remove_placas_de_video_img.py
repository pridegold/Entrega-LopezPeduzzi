# Generated by Django 4.1.2 on 2022-11-28 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_placas_de_video_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placas_de_video',
            name='img',
        ),
    ]
