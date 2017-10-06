# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Album(models.Model):
    album_logo = models.FileField()
    