from django.db import models

from member.models import CustomMember, Worker

class Job(models.Model):
    status = models.CharField(max_length=15, default='Open')
    member = models.ForeignKey(CustomMember, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    job_description = models.CharField(max_length=255)
    location = models.CharField(max_length=50)
    price = models.IntegerField()
    contact_number = models.IntegerField(null=True)


class Contract(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
