from .models import Books
from rest_framework import serializers

class BookSerializers(serializers.Serializer):
    class Meta:
        model = Books
        fields = '__all__'