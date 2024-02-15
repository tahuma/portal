import uuid

from django.db import models


# Create your models here.


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
