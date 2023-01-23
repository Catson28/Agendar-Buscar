from django.db import models

# Create your models here.
class matter(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)


class post(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    matter=models.ForeignKey(matter, on_delete=models.CASCADE)

class image(models.Model):
    name=models.CharField(max_length=50)
    matter=models.ForeignKey(matter, on_delete=models.CASCADE)
    post=models.ForeignKey(post, on_delete=models.CASCADE)

class text(models.Model):
    name=models.CharField(max_length=50)