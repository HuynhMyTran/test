# Generated by Django 4.1.7 on 2023-03-03 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0005_tag_lesson"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="tags",
            field=models.ManyToManyField(related_name="lessons", to="courses.tag"),
        ),
    ]
