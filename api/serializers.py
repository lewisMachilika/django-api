from rest_framework import serializers
from .models import CustomUser

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        exclude = ('groups', 'user_permissions','is_superuser','password')
