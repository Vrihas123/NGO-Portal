# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserDetail
# Register your models here.

class UserDetailAdmin(admin.ModelAdmin):
    list_display = ['name','username','mobile','aadhar']
admin.site.register(UserDetail,UserDetailAdmin)    