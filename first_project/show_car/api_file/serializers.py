from rest_framework import serializers

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length = 40)
    description = serializers.CharField(max_length = 500)
    active = serializers.BooleanField(read_only=True)