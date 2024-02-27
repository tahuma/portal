import uuid

from django.db import models


# Create your models here.

# For the catalog

class Type(models.Model):
    """
    A model to store types in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Catalog(models.Model):
    """
    A model to store catalogs in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    """
    A model to store places in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Library(models.Model):
    """
    A model to store libraries in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    description = models.TextField()
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Collection(models.Model):
    """
    A model to store collections in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    A model to store books in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    shelfmark = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    A model to store tags in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    """
    A model to store authors in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Manuscript(models.Model):
    """
    A model to store items in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    types = models.ForeignKey(Type, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    shelfmark = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    A model to store categories in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Metadata(models.Model):
    """
    A model to store metadata in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.CharField(max_length=100)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.key


class Text(models.Model):
    """
    A model to store texts in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    text = models.TextField()
    file = models.FileField(upload_to='uploads/texts/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.title
