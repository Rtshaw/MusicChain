from django.db import models
from django.utils import timezone
import uuid

from user.models import UserProfile


class Music(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='上傳者', null=True)
    musicname = models.CharField(max_length=20, verbose_name='音樂名稱')
    singername = models.CharField(max_length=20, verbose_name='歌手名稱')
    body = models.TextField(blank=True, verbose_name='音樂說明')
    update_time = models.DateTimeField(default=timezone.now,verbose_name='上傳時間')
    music = models.FileField(blank=False, upload_to='resources/music/%Y/%m/%d/', verbose_name='音樂上傳路徑')
    token = models.UUIDField(db_index=True, default=uuid.uuid4)

    class Meta:
        verbose_name = r'音樂資訊'   #別稱c
        verbose_name_plural = verbose_name  #單數別稱

    def __str__(self):
        return self.musicname

class Transaction(models.Model):
    sourceaddr = models.CharField(max_length=58, verbose_name='來源錢包')
    distinationaddr = models.CharField(max_length=58, verbose_name='目的錢包')
    amount = models.CharField(max_length=100,blank=True, verbose_name='金額')
    transaction_time = models.DateTimeField(default=timezone.now,verbose_name='交易時間')
    musictoken = models.ForeignKey('Musicblock', on_delete=models.CASCADE, verbose_name='所屬音樂區塊')
    token = models.UUIDField(db_index=True, default=uuid.uuid4)
    Transactionblock = models.ForeignKey('Transactionblock', on_delete=models.CASCADE, verbose_name='所屬交易區塊',null=True)

    class Meta:
        verbose_name = r'交易資訊'   #別稱c
        verbose_name_plural = verbose_name  #單數別稱

    def __str__(self):
        return self.musictoken.musicname

#一首音樂會綁一個音樂區塊
class Musicblock(models.Model):
    timestamp = models.DateTimeField(default=timezone.now,verbose_name='建立時間')
    music_hash = models.CharField(max_length=20, verbose_name='mp3的hash')
    music_token = models.ForeignKey(Music, on_delete=models.CASCADE, verbose_name='所屬音樂')
    previous_hash = models.CharField(max_length=20, verbose_name='創始區塊hash', default='1')
    self_hash = models.CharField(max_length=20, verbose_name='自己區塊hash',null=True,blank =True)
    musicblock_hash = models.UUIDField(db_index=True, default=uuid.uuid4, verbose_name='音樂區塊的編號(不重複的、會自動產生的)')
    music_proof = models.CharField(max_length=20, verbose_name='工作量證明', default='100')

    class Meta:
        verbose_name = r'音樂區塊'   #別稱c
        verbose_name_plural = verbose_name  #單數別稱

    def __str__(self):
        return self.music_hash

#一個交易區塊會有很多交易
class Transactionblock(models.Model):
    timestamp = models.DateTimeField(default=timezone.now,verbose_name='建立時間')
    transactionblock_hash = models.UUIDField(db_index=True, default=uuid.uuid4, verbose_name='交易區塊的編號(不重複的、會自動產生的)')
    previous_hash = models.CharField(max_length=20, verbose_name='上一個hash', default='1')
    music_proof = models.CharField(max_length=20, verbose_name='工作量證明')
    self_hash = models.CharField(max_length=20, verbose_name='自己區塊hash',null = True,blank =True)

    class Meta:
        verbose_name = r'交易區塊'   #別稱c
        verbose_name_plural = verbose_name  #單數別稱

    def __str__(self):
        return self.transactionblock_hash