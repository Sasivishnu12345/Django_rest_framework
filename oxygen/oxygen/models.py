from django.db import models
class permission(models.Model):
	ParentsApproval=models.CharField(max_length=50)
	ClasscoordinatorApproval=models.CharField(max_length=50)
	WardenApproval=models.CharField(max_length=40)
	HODApproval=models.CharField(max_length=40)
class task(models.Model):
	project=models.CharField(max_length=50)
	tasks=models.CharField(max_length=50)
	task_description=models.CharField(max_length=255)
	due_date=models.CharField(max_length=15)
	documents=models.CharField(max_length=50)