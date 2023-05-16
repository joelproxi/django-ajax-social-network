from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer, RelatedField

from apps.models import Notification


class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields ='__all__'
        

class TargetSerializer(RelatedField):
    
    def to_representation(self, value):
        return value.content
    

class NotificationSerialiser(ModelSerializer):
    target = TargetSerializer(read_only=True)
    class Meta:
        model = Notification
        fields = ['id',
                  'read',
                  'user',
                  'target',
                  'created',
                  'action']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = {
            'username': instance.user.username,
            'id': instance.id,
        }
        return data