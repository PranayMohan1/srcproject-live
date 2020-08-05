from rest_framework import serializers
from activity.models import Member,Period

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields=['start_time','end_time']

class MemberSerializer(serializers.ModelSerializer):
    activity_periods=PeriodSerializer(many=True)
    
    class Meta:
        model = Member
        fields=['id','real_name','tz','activity_periods']

    def create(self, validated_data):
        activity_periods_data = validated_data.pop('activity_periods')
        member = Member.objects.create(**validated_data)
        for periodd in activity_periods_data:
            Period.objects.create(member=member, **periodd)
        return member
    
    def update(self, instance, validated_data):
        activity_periods_data = validated_data.pop('activity_periods')
        periodss = (instance.activity_periods).all()
        periodss = list(periodss)
        instance.id = validated_data.get('id', instance.id)
        instance.real_name = validated_data.get('real_name', instance.real_name)
        instance.tz = validated_data.get('tz', instance.tz)
        instance.save()

        for apdata in activity_periods_data:
            pd = periodss.pop(0)
            pd.start_time = apdata.get('start_time', pd.start_time)
            pd.end_time = apdata.get('end_time', pd.end_time)
            pd.save()
        return instance

