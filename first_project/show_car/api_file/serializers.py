from rest_framework import serializers
from ..models import carList,ShowRoom


def alphanumberic(value):
    if not str(value).isalnum():
        raise serializers.ValidationError("Only alphanumeric chanacters are allowed")

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = carList
        fields = "__all__"

class ShowRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowRoom
        fields = "__all__"


    """
    This is for normal serializer
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length = 40)
    description = serializers.CharField(max_length = 500)
    active = serializers.BooleanField(read_only=True)
    chassisNumber = serializers.CharField(validators = [alphanumberic])
    price = serializers.DecimalField(max_digits=9,decimal_places=2)

    def create(self, validated_data):
        return carList.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.chassisNumber = validated_data.get('chassisNumber',instance.chassisNumber)
        instance.price = validated_data.get('price',instance.price)
        instance.save()
        return instance
    """
    def validate_price(self,value):
        if value<20000.00:
            raise serializers.ValidationError("Price must be greater than 200")
        return value
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description shouold be difference')
        return data
        