from django.db import models
from django.conf import settings 
from django.utils import timezone
from membership import constants
from core.models import BaseModel, BaseModelWithSoftDelete, Client, ClientUser

class Family(BaseModel):
    name = models.CharField(max_length=100)

class MemberStatus(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Member(BaseModelWithSoftDelete):
    user = models.OneToOneField(ClientUser, null=True, blank=True, default=None, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    join_date = models.DateField(null=True, blank=True, default=timezone.now())
    status = models.IntegerField(choices=constants.STATUS_CHOICES, default=constants.STATUS_ACTIVE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    sex = models.IntegerField(choices=constants.SEX_CHOICES)
    age = models.IntegerField()
    email = models.EmailField()
    family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.user.username
    

