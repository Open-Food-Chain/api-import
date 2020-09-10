from django.db.models import (
    Model,
    CharField,
    UUIDField,
)
import uuid

# Create your models here.


class Batch(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=40)
    integrity_details = CharField(max_length=40)


class Integrity(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=50)
