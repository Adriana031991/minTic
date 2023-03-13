from rest_framework import serializers
from appTienda.models.user import User

class UserUpdateSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ['name']

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.password = validated_data.get('password', instance.password)
    instance.save()
    return instance