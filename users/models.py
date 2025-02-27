from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Користувач повинен мати email")
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=[('admin', 'Адміністратор'), ('user', 'Користувач')], default='user')

    objects = CustomUserManager()  # Додаємо власний менеджер

    from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва продукту")
    description = models.TextField(verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Зображення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    
    def __str__(self):
        return self.name

    
    
