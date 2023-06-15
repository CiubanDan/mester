from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomMember(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    member_type = ((False, 'Member'), (True, "Worker"))
    is_worker = models.BooleanField(choices=member_type, default=False)
    phone_number = models.CharField(max_length=10)
    username = None

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Category(models.Model):
    category_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.category_name}'


class Worker(models.Model):
    member = models.ForeignKey(CustomMember, on_delete=models.CASCADE, related_name='worker')
    worker_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    about_me = models.CharField(max_length=255, null=True)
    is_premium = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name} {self.about_me}"


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
