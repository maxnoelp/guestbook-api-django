from rest_framework import serializers
from .models import guestBook

class bookSerializers(serializers.ModelSerializer):
    class Meta:
        model = guestBook
        fields = ['id', 'name', 'text', 'date', 'link']