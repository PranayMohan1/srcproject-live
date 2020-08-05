from django.db import models
import pytz
timezone=[(tz,tz) for tz in pytz.all_timezones]

class Member(models.Model):
    id = models.CharField(max_length=11,blank=False,primary_key=True)
    real_name = models.CharField(max_length=100,blank=False,unique=False)
    tz = models.CharField(choices=timezone,default='Asia/Kolkata',max_length=100,unique=False)
    
    def __str__(self):
        return self.real_name

class Period(models.Model):
    member = models.ForeignKey(Member,related_name='activity_periods',on_delete=models.CASCADE,default='')
    start_time = models.DateTimeField(unique=False)
    end_time = models.DateTimeField(unique=False)

    def __str__(self):
        return self.member_id

 