from rest_framework import status
from rest_framework.views import APIView
from activity.models import Member,Period
from activity.serializers import PeriodSerializer
from activity.serializers import MemberSerializer
from django.http import Http404
from rest_framework.response import Response

class MemberList(APIView):
    def get(self,request,format=None):
        members = Member.objects.all()
        memberSerialized = MemberSerializer(members,many=True)
        return Response(memberSerialized.data)
    
    def post(self,request,format=None):
        serializer=MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

class MemberDetail(APIView):
    def get_object(self,pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404
    def get(self,request,pk,format=None):
        member=self.get_object(pk)
        serializer=MemberSerializer(member)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        member=self.get_object(pk)
        serializer=MemberSerializer(member,data=request.data)
        if serializer.valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        member=self.get_object(pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

