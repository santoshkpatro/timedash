import uuid
from django.db import models
from timedash.db.models.base import BaseCharTimestampModel
from timedash.db.models.merchant import Merchant
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class User(BaseCharTimestampModel, AbstractBaseUser):
    class Role(models.TextChoices):
        ADMIN = ("admin", "Admin")
        OWNER = ("owner", "Owner")
        STAFF = ("staff", "Staff")

    merchant = models.ForeignKey(
        Merchant,
        on_delete=models.CASCADE,
        related_name="users",
        blank=True,
        null=True,
    )
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    role = models.CharField(max_length=5, choices=Role.choices, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_password_expired = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name"]

    class Meta:
        db_table = "users"

    def __str__(self) -> str:
        return self.email

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = "user_" + uuid.uuid4().hex[:15]

            if not self.username:
                self.username = uuid.uuid4().hex[:20]
        return super().save(*args, **kwargs)
