# Generated by Django 4.2.5 on 2023-09-23 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoderBlogApp', '0005_alter_blog_post_alter_blog_quote_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post',
            field=models.TextField(max_length=1000),
        ),
    ]