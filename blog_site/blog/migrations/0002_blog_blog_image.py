# Generated by Django 4.2.5 on 2023-09-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="blog_image",
            field=models.ImageField(blank=True, null=True, upload_to="blog_images/"),
        ),
    ]