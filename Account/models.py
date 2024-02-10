import uuid  # Імпорт модуля uuid

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.password_validation import validate_password
from .validators import validate_image_file_extension  # Імпорт вашого власного валідатора

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)  # Використання uuid.uuid4
    username = models.CharField(max_length=150, unique=True, validators=[UnicodeUsernameValidator])
    email = models.EmailField(unique=True, validators=[EmailValidator])
    password = models.CharField(max_length=128, validators=[validate_password])
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, validators=[validate_image_file_extension])
    email_confirmed = models.BooleanField(default=False)
    # Поле для зв'язку з групами
    groups = models.ManyToManyField(Group, related_name='custom_users')
    # Поле для зв'язку з правами користувача
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate fields before saving
        super().save(*args, **kwargs)



