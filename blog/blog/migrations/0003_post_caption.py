# Generated by Django 2.2.24 on 2021-06-27 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_img_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='caption',
            field=models.TextField(default=11),
            preserve_default=False,
        ),
    ]
