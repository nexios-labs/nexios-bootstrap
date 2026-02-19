import uuid
from tortoise import fields
from tortoise.models import Model


def generate_uid():
    return uuid.uuid4().hex


class BaseModel(Model):
    id = fields.CharField(
        max_length=32,
        pk=True,
        default=generate_uid
    )

    created_at = fields.DatetimeField(
        auto_now_add=True
    )

    updated_at = fields.DatetimeField(
        auto_now=True
    )

    is_deleted = fields.BooleanField(
        default=False
    )

    class Meta:
        abstract = True