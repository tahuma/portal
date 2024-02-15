# Generated by Django 4.1.11 on 2024-02-14 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("synopsis", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="text",
            name="url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="text",
            name="created_by",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="text",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to="uploads/texts/"),
        ),
        migrations.AlterField(
            model_name="text",
            name="updated_by",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
