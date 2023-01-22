from django.db import models

# Create your models here.


class packages(models.Model):
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)

class albums(models.Model):
    type=models.CharField(max_length=20)
    quantty=models.IntegerField()
    size=models.CharField(max_length=30)
    price=models.CharField(max_length=20)
    package=models.ManyToManyField("packages") # exemplo de relacionamento de muitos para muitos
    # idAlbum=models.OneToOneField(packages, on_delete=models.CASCADE) # exemplo de relacionamento de um para um
    # idAlbum=models.ForeignKey(packages, on_delete=models.CASCADE) # exemplo de relacionamento de um para muitos

class frames(models.Model):
    type=models.CharField(max_length=20)
    size=models.CharField(max_length=30)
    price=models.CharField(max_length=20)
    package=models.ManyToManyField("packages")

class pendrives(models.Model):
    type=models.CharField(max_length=30)
    capacity=models.CharField(max_length=20)
    price=models.CharField(max_length=30)
    package=models.ManyToManyField("packages")

class photographs(models.Model):
    type=models.CharField(max_length=20)
    size=models.CharField(max_length=30)
    price=models.CharField(max_length=20)
    albums=models.ManyToManyField("albums")
    package=models.ManyToManyField("packages")
    pendrives=models.ManyToManyField("pendrives")

class videos(models.Model):
    type=models.CharField(max_length=50)
    duration=models.TimeField()
    format=models.CharField(max_length=30)
    price=models.CharField(max_length=20)
    package=models.ForeignKey(packages, on_delete=models.CASCADE)
    pendrives=models.ForeignKey(pendrives, on_delete=models.CASCADE)

class professionals(models.Model):
    area=models.CharField(max_length=30)
    office=models.CharField(max_length=50)
    package=models.ManyToManyField("packages")

class interested(models.Model):
    name=models.CharField(max_length=50)
    source=models.CharField(max_length=50)
    package=models.ManyToManyField("packages")


class customers(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=15)
    interested=models.OneToOneField(interested, on_delete=models.CASCADE)

class celebrants(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=15)
    customers=models.ForeignKey(customers, on_delete=models.CASCADE)

class locations(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    contact=models.CharField(max_length=50)
    package=models.ManyToManyField("packages")

class agendas(models.Model):
    action=models.CharField(max_length=50)
    star_date=models.DateField()
    end_date=models.DateField()
    icon=models.CharField(max_length=50)
    status=models.BooleanField(max_length=50)

class calendars_candstudio(models.Model):
    agendas=models.ForeignKey(agendas, on_delete=models.CASCADE)
    package=models.ForeignKey(packages, on_delete=models.CASCADE)
    customers=models.ForeignKey(customers, on_delete=models.CASCADE)
