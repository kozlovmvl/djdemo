from django.core.exceptions import ValidationError
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    city = models.ForeignKey("users.City", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    MIN_LENGTH_USERNAME = 5

    class Meta:
        db_table = "users"

    def __str__(self) -> str:
        return str(self.username)

    def clean(self) -> None:
        if len(self.username) < self.MIN_LENGTH_USERNAME:
            raise ValidationError(
                f"Length of username should be more {self.MIN_LENGTH_USERNAME}"
            )

    def save(self, *args, **kwargs) -> None:
        self.clean()
        super().save(*args, **kwargs)


class City(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "cities"

    def __str__(self) -> str:
        return str(self.name)
