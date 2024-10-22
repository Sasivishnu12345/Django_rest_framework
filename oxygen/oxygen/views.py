from rest_framework import viewsets
from .serializers import permissionserializer,taskserializer
from .models import permission,task
class permissionviewset(viewsets.ModelViewSet):
	queryset=permission.objects.all()
	serializer_class=permissionserializer
class taskviewset(viewsets.ModelViewSet):
	queryset=task.objects.all()
	serializer_class=taskserializer