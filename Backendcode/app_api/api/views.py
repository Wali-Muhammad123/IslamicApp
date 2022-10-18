from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import AnnouncementsSerializer,prayerSerializer
from .models import Announcements,prayer
# Create your views here.
class AnnouncementsView(APIView):
    def get(self,request):
        announcements=Announcements.objects.all()
        serializer=AnnouncementsSerializer(announcements,many=True)
        return Response(serializer.data)
class prayerView(APIView):
    def get(self,request):
        prayers=prayer.objects.all()
        serializer=prayerSerializer(prayers,many=True)
        return Response(serializer.data)
class updateAnnouncement(APIView):
    def get(self,request):
        announcements=Announcements.objects.all()
        serializer=AnnouncementsSerializer(announcements,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=AnnouncementsSerializer(announcements,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    def put(self,request,pk):
        announcements=Announcements.objects.get(pk=pk)
        serializer=AnnouncementsSerializer(announcements,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)
    def delete(self,request,pk):
        announcements=Announcements.objects.get(pk=pk)
        announcements.delete()
        return Response("Announcement Deleted")
class updatePrayer(APIView):
    def get(self,request):
        prayers=prayer.objects.all()
        serializer=prayerSerializer(prayers,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=prayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    def put(self,request,pk):
        prayers=prayer.objects.get(pk=pk)
        serializer=prayerSerializer(prayers,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)
    def delete(self,request,pk):
        prayers=prayer.objects.get(pk=pk)
        prayers.delete()
        return Response("Prayer Deleted")

    