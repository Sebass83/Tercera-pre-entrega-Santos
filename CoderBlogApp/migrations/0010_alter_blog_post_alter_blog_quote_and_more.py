# Generated by Django 4.2.5 on 2023-09-23 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoderBlogApp', '0009_alter_blog_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='quote',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='blogsummary',
            name='description',
            field=models.CharField(max_length=400),
        ),
    ]
