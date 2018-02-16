import hashlib
import json
import os
from time import time
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse
from uuid import uuid4
# from mp3hash import mp3hash
import random
import ecdsa
import base58
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render


#個人詳細頁面
from django.urls import reverse
from django.views import generic

from .forms import UserForm
from .models import UserProfile


class UserProfileDetail(generic.DetailView):
    model = UserProfile
    template_name = 'user_detail.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(QuestionDetail, self).get_context_data(*args, **kwargs)
    #     context['Question_list'] = Question.objects.all()
    #     question = get_object_or_404(Question, qtoken=self.kwargs['questiontoken'])
    #     context['Answer_list'] = Answer.objects.filter(aquestion=question)
    #     return context

    #取得使用者物件的方法
    def get_object(self):
        return self.model.objects.filter(token=self.kwargs['token'])

    def get(self, request, *args, **kwargs):
        # print(self.get_object().username)
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user in self.get_object() :
           return super().get(request, *args, **kwargs)
        else:
            messages.warning(self.request, '無此權限')
            return HttpResponseRedirect(reverse('index'))

class SignUp(generic.CreateView):
    model = UserProfile
    form_class = UserForm
    template_name = 'user_form.html'

    def get_success_url(self):
        messages.success(self.request, '註冊成功')
        return reverse('index')
#註冊之後會自動產生私鑰跟錢包地址
    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        private_key = hex(random.randint(1, 8288608480668846482228684402464624222246648088028668608040264462))[2:]
        if len(private_key) != 64:
            for i in range(64 - len(private_key)):
                private_key = '0' + private_key

        private_key = bytes.fromhex(private_key)

        sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
        vk = b'\x04' + sk.verifying_key.to_string()

        ek = hashlib.sha256(vk).digest()

        ripemd160 = hashlib.new('ripemd160')
        ripemd160.update(ek)
        rk = b'\x00' + ripemd160.digest()

        checksum = hashlib.sha256(hashlib.sha256(rk).digest()).digest()[0:4]
        public_key = rk + checksum

        wallet_address = base58.b58encode(public_key)
        self.object.prvateKey = private_key
        self.object.publicKey = public_key
        self.object.address = wallet_address
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
