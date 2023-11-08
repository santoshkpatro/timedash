import uuid
from django.db import models
from timedash.db.models.base import BaseCharTimestampModel
from timedash.db.models.merchant import Merchant


class Key(BaseCharTimestampModel):
    class Mode(models.TextChoices):
        MAIN = ("main", "Main")
        SANDBOX = ("sandbox", "Sandbox")

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="keys")
    secret = models.CharField(max_length=100, blank=True)
    last_used = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    mode = models.CharField(max_length=10, choices=Mode.choices)

    class Meta:
        db_table = "keys"

    def __str__(self) -> str:
        return self.id
    
    def save(self, *args, **kwargs):
        if self._state.adding:
            if self.mode == 'main':
                self.id = "key_main_" + uuid.uuid4().hex[:11]
            else:
                self.id = 'key_sandbox_' + uuid.uuid4().hex[:8]

            if not self.secret:
                self.secret = uuid.uuid4().hex
        return super().save(*args, **kwargs)