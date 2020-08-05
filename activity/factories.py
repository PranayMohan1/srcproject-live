from activity.models import Member,Period
import random
from activity.names import Names
import pytz
import factory
from datetime import datetime,date,time,timedelta
from django.utils.timezone import make_aware
timezone=[tz for tz in pytz.all_timezones]
nms=[name for name in Names.names]



class MemberFactory():
    
    def create(self):
        mem = Member()
        mem.id = 'W'+str(random.sample(range(11111111,99999999),1)[0])
        mem.real_name = random.choice(nms)
        mem.tz = random.choice(timezone)
        mem.save()
    

class PeriodFactory():
    
    def create(self):
        pd=Period()
        memlist = []
        for obj in Member.objects.all():
            memlist.append(obj.pk)

        pd.member = Member.objects.get(pk=random.choice(memlist))
        d = date(random.randint(2000,2020),random.randint(1,12),random.randint(1,28))
        ts = time(random.randint(0,23),random.randint(0,59),random.randint(0,59))
        dt1 = datetime.combine(d,ts)
        hours=7
        hours_added=timedelta(hours=hours)
        dt2=dt1+hours_added
        
        pd.start_time = dt1.strftime("%Y-%m-%d %H:%M:%S")
        pd.end_time = dt2.strftime("%Y-%m-%d %H:%M:%S")
        pd.save()
    

