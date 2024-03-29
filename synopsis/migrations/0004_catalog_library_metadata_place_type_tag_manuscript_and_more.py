# Generated by Django 4.1.11 on 2024-02-27 19:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("synopsis", "0003_text_enabled"),
    ]

    operations = [
        migrations.CreateModel(
            name="Catalog",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Library",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "catalog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="synopsis.catalog"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Metadata",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("key", models.CharField(max_length=100)),
                ("value", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.CharField(blank=True, max_length=100, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("updated_by", models.CharField(blank=True, max_length=100, null=True)),
                ("enabled", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Type",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "catalog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="synopsis.catalog"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Manuscript",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("shelfmark", models.CharField(max_length=100)),
                ("url", models.URLField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "catalog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="synopsis.catalog"
                    ),
                ),
                (
                    "library",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="synopsis.library"
                    ),
                ),
                (
                    "types",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="synopsis.type"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="library",
            name="place",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="synopsis.place"
            ),
        ),
        migrations.CreateModel(
            name="Collection",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "catalog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="synopsis.catalog"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "catalog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="synopsis.catalog"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("shelfmark", models.CharField(max_length=100)),
                ("url", models.URLField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "catalog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="synopsis.catalog"
                    ),
                ),
                (
                    "collection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="synopsis.collection"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "catalog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="synopsis.catalog"
                    ),
                ),
            ],
        ),
    ]
