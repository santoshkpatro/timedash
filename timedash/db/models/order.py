import uuid
from django.db import models
from timedash.db.models.base import BaseCharTimestampModel


class Order(BaseCharTimestampModel):
    class Status(models.TextChoices):
        CREATED = ("created", "Created")
        ATTEMPTED = ("attempted", "Attempted")
        PAID = ("paid", "Paid")

    merchant_id = models.CharField(max_length=20, blank=True, db_index=True)
    amount = models.IntegerField()
    currency = models.CharField(max_length=3)
    notes = models.JSONField(blank=True, null=True)
    identifier = models.CharField(max_length=100, blank=True, null=True)
    attempts = models.IntegerField(default=0)
    amount_due = models.IntegerField(blank=True)
    amount_paid = models.IntegerField(blank=True)
    partial_payment = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.CREATED
    )

    class Meta:
        db_table = "orders"

    def __str__(self) -> str:
        return self.id

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = "order_" + uuid.uuid4().hex[:14]

            if not self.amount_paid:
                self.amount_paid = self.amount

            if not self.amount_due:
                self.amount_due = 0
        return super().save(*args, **kwargs)
