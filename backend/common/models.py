from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UserMixin(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user1")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
