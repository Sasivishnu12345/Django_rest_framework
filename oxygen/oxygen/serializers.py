from rest_framework import serializers
from .models import permission,task
class permissionserializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=permission
		fields=('ParentsApproval','ClasscoordinatorApproval','WardenApproval','HODApproval')
class taskserializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=task
		fields=('project','tasks','task_description','due_date','documents')