from django.contrib.auth.models import AbstractUser
from django.db import models

#
# class MyUser(AbstractUser):
#     pass


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Specialist(models.Model):
    title = models.CharField(max_length=250)
    age = models.IntegerField(default='')
    gender = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    likes = models.IntegerField(default='')
    comments = models.CharField(max_length=250)
    front_image = models.CharField(max_length=1000)
    first_image = models.CharField(max_length=1000, default='')
    second_image = models.CharField(max_length=1000, default='')
    third_image = models.CharField(max_length=1000, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="specialists")

    class Meta:
        verbose_name = 'Specialist'
        verbose_name_plural = 'Specialists'


class Comment(models.Model):
    title = models.CharField(max_length=100, default='default title')
    text = models.CharField(max_length=1000, default='default text')
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='specialists')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Manager(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }
