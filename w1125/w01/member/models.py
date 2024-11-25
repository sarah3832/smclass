from django.db import models
# import datetime  # default=datetime.datetime.now()  <-- 2번적어야함
from datetime import datetime  # datetime.now()

class Member(models.Model):
  id = models.CharField(max_length=50,primary_key=True)
  pw = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  nicName = models.CharField(max_length=100)
  tel = models.CharField(max_length=20,default='010-0000-0000')
  gender = models.CharField(max_length=10,default='남자')
  hobby = models.CharField(max_length=50,default='game')
  mdate = models.DateTimeField(auto_now=True)
  # mdate = models.DateTimeField(default=datetime.now())

  def __str__(self):
    return f"{self.id},{self.name},{self.mdate}"