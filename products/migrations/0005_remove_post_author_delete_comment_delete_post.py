# Generated by Django 4.1.7 on 2023-04-06 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_post_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
