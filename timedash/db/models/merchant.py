import uuid
from django.db import models
from timedash.db.models.base import BaseCharTimestampModel


class Merchant(BaseCharTimestampModel):
    class Status(models.TextChoices):
        ACTIVE = ("active", "Active")
        PENDING = ("pending", "Pending")
        BLOCKED = ("blocked", "Blocked")

    name = models.CharField(max_length=100)
    country = models.CharField(max_length=2)
    currency = models.CharField(max_length=3, blank=True)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.PENDING
    )

    class Meta:
        db_table = "merchants"

    def __str__(self) -> str:
        return self.id

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = uuid.uuid4().hex[:6].upper()
        return super().save(*args, **kwargs)
