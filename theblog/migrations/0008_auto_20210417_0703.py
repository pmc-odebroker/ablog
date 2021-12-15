# Generated by Django 3.1.7 on 2021-04-17 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click The Link Above To Read Blog Post.....', max_length=255),
        ),
    ]
