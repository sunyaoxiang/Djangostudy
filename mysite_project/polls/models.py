# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys;
reload(sys);
sys.setdefaultencoding("utf8")


import datetime
from django.db import models
# from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# @python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length = 300)
    pub_date = models.DateField('date published')
    pub_time = models.TimeField()

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)


# @python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
    cho_date = models.DateField('date choice')

    def __str__(self):
        return self.choice_text