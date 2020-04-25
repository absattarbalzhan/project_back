from django.db import models


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
