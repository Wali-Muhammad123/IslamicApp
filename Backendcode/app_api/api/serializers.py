from rest_framework import serializers
from .models import Announcements,prayer
class AnnouncementsSerializer(serializers.Serializer):
    class meta:
        model=Announcements
        fields='__all__'
class prayerSerializer(serializers.Serializer):
    class meta:
        model=prayer
        fields='__all__'