from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import SoftDeleteManager, UserManager
from django.utils import timezone
from . import constants

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModelWithSoftDelete(BaseModel):
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):  # pragma: no cover
        self.deleted_at = None
        self.save()

class Client(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        

class ClientDetail(BaseModel):
    client = models.OneToOneField(Client, on_delete=models.PROTECT)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_demo = models.BooleanField(default=False)
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return self.client.name

    class Meta:
        unique_together = ('client', 'email')
        
class ClientUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    user_type = models.IntegerField(choices=constants.USER_TYPE_CHOICES, default=constants.CLIENT_ADMIN)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
