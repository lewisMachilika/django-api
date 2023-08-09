from rest_framework import viewsets
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
