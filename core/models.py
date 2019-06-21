import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    is_active = models.BooleanField(default=False)

    inserted_since = models.DateField(auto_now_add=True)
    inserted_by = models.ForeignKey('User', related_name="entries_inserted", null=True, on_delete=models.PROTECT)

    last_updated_since = models.DateField(auto_now=True)
    updated_by = models.ForeignKey('User', related_name="entries_updated", null=True, on_delete=models.PROTECT)

    class Meta:
        abstract = True
