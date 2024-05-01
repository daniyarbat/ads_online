from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


NULLABLE = {
    "null": True,
    "blank": True
}


class UserRoles:
    # TODO закончите enum-класс для пользователя
    ADMIN = "admin"
    USER = "user"


roles_choices = (
    (UserRoles.ADMIN, "Admin"),
    (UserRoles.USER, "User"),
)


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту
    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    phone = models.CharField(max_length=15, verbose_name='телефон')
    email = models.EmailField(unique=True, verbose_name="почта")
    role = models.CharField(max_length=10, default=UserRoles.USER, choices=roles_choices, verbose_name="роли")
    image = models.ImageField(upload_to="profile_images", verbose_name="фото", **NULLABLE)
    is_active = models.BooleanField(default=False)

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    # также для работы модели пользователя должен быть переопределен
    # менеджер объектов
    objects = UserManager()
