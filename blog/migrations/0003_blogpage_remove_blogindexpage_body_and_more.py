# Generated by Django 4.1.11 on 2023-09-06 16:42

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
        ("blog", "0002_blogindexpage_body_blogindexpage_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("date", models.DateField(verbose_name="Post date")),
                ("intro", models.CharField(max_length=250)),
                ("body", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.RemoveField(
            model_name="blogindexpage",
            name="body",
        ),
        migrations.RemoveField(
            model_name="blogindexpage",
            name="date",
        ),
        migrations.AlterField(
            model_name="blogindexpage",
            name="intro",
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]