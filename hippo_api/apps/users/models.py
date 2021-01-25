from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    # avatar = models.ImageField(upload_to='touxiang', )
    phone = models.CharField(max_length=15, verbose_name='手机号码')

    class Meta:
        db_table = 'hippo_user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
