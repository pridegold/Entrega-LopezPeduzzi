# Generated by Django 4.1.3 on 2022-11-25 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='placas_de_video',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
