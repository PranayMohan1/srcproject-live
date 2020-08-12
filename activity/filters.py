import django_filters

from .models import Member,Period

class MemberFilter(django_filters.FilterSet):
    class Meta:
        model = Member
        fields = {
            'id':['exact'],
            'real_name':['icontains'],
            'tz':['icontains'],
        }
class PeriodFilter(django_filters.FilterSet):
    class Meta:
        model=Period
        fields={
            'member':['exact'],
            'start_time':['gt','gte','lt','lte'],
            'end_time':['gt','gte','lt','lte'],
        }