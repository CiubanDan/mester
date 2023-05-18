from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomMember(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    member_type = ((False, 'Member'), (True, "Worker"))
    is_worker = models.BooleanField(choices=member_type)
    phone_number = models.CharField(max_length=10)
    username = None



class Category(models.Model):
    category_name = models.CharField(max_length=50, null=True)


class Worker(models.Model):
    member = models.OneToOneField(CustomMember, on_delete=models.CASCADE, related_name='worker')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    is_premium = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)


class Review(models.Model):
    stars_options = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    member = models.ForeignKey(CustomMember, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=stars_options)


class Pay(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    amount = models.TextField()
    pay_date = models.DateTimeField(auto_now_add=True)


class Chat(models.Model):
    member = models.ForeignKey(CustomMember, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    message = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)
