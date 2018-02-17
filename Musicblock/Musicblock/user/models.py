from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid

# Create your models here.
class UserProfile(AbstractUser):
    #內建的欄位:名字、信箱、帳號、密碼
    #額外增加的欄位有身分證(存hash)
    # 上傳身分證圖
    ssn = models.CharField(max_length=10, null=False, blank=False, verbose_name=u'身分證字號',unique=True)
    file = models.FileField(blank=False, upload_to='resources/%Y/%m/%d/', verbose_name='身分證照')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='female',
                              verbose_name=u'性別')
    prvateKey = models.CharField(max_length=64, null=True, blank=True, verbose_name=u'私鑰',unique=True)
    publicKey = models.CharField(max_length=64, null=True, blank=True, verbose_name=u'公鑰',unique=True)
    address = models.CharField(max_length=58, null=True, blank=True, verbose_name=u'錢包',unique=True)
    token = models.UUIDField(db_index=True, default=uuid.uuid4)
    class Meta:
        verbose_name = r'使用者資訊'   #別稱c
        verbose_name_plural = verbose_name  #單數別稱

    def __str__(self):
        return self.username