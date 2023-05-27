from django.db import models, transaction
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible

# Create your models here.

class CustomAccountManger(BaseUserManager):
    @transaction.atomic
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")
        return self.create_user(username, password, **extra_fields)

    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_("You must provide an username"))

        user = self.model(
            username=username,
            password=password,
            phone=extra_fields.pop("phone", None),
            email=extra_fields.pop("email", None),
            **extra_fields
        )
        user.set_password(password)

    
        user.save()
        return user

@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r'^[\w.@+-]+\Z'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and @/./+/-/_ characters.'
    )
    flags = 0

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    user_id = models.BigAutoField(
        primary_key=True,
        unique=True,
        editable=False,
        verbose_name="user_id",
    )
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        ),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=45, blank=True)
    last_name = models.CharField(_("last name"), max_length=45, blank=True)
    
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    profile_img = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active.'
            'Unselect this instead of deleting accounts.'
        ),
    )
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    

    objects = CustomAccountManger()
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = "users"
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username