from django.db import models
# from django.utils import timezone

# Aqui sao criadas a models
class Package(models.Model):
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)
    def __str__(self):  #funcao para mostrar o nome  e o preco em vez da palavra object
        return "%s %s" % (self.name, self.price)

class Album(models.Model):
    type=models.CharField(max_length=20)
    quantty=models.IntegerField()
    size=models.CharField(max_length=30)
    price=models.CharField(max_length=20)
    package=models.ManyToManyField("Package") #Exemplo de relacionamento de muitos para muitos
    # idAlbum=models.OneToOneField(Package, on_delete=models.CASCADE) # exemplo de relacionamento de um para um
    # idAlbum=models.ForeignKey(Package, on_delete=models.CASCADE) # exemplo de relacionamento de um para muitos

class Frame(models.Model):
    type=models.CharField(max_length=20)
    size=models.CharField(max_length=30)
    price=models.CharField(max_length=20)
    package=models.ManyToManyField("Package")

class Pendrive(models.Model):
    type=models.CharField(max_length=30)
    capacity=models.CharField(max_length=20)
    price=models.CharField(max_length=30)
    package=models.ManyToManyField("Package")

class Photograph(models.Model):
    type=models.CharField(max_length=20)
    size=models.CharField(max_length=30)
    price=models.CharField(max_length=20)
    Album=models.ManyToManyField("Album")
    package=models.ManyToManyField("Package")
    Pendrive=models.ManyToManyField("Pendrive")

class Video(models.Model):
    type=models.CharField(max_length=50)
    duration=models.TimeField()
    format=models.CharField(max_length=30)
    price=models.CharField(max_length=20)
    package=models.ForeignKey(Package, on_delete=models.CASCADE)
    Pendrive=models.ForeignKey(Pendrive, on_delete=models.CASCADE)

class Professional(models.Model):
    area=models.CharField(max_length=30)
    office=models.CharField(max_length=50)
    package=models.ManyToManyField("Package")

class Interested(models.Model):
    name=models.CharField(max_length=50)
    source=models.CharField(max_length=50)
    package=models.ManyToManyField("Package")


class Client(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=15)
    Interested=models.OneToOneField(Interested, on_delete=models.CASCADE)

class Celebrant(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=15)
    Client=models.ForeignKey(Client, on_delete=models.CASCADE)

class Place(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    contact=models.CharField(max_length=50)
    package=models.ManyToManyField("Package")

class Schedule(models.Model):
    action=models.CharField(max_length=50)
    # star_date=models.DateField(auto_now_add=True, default=timezone.now())
    # end_date=models.DateField(auto_now_add=True, default=timezone.now())
    icon=models.CharField(max_length=50)
    status=models.BooleanField(max_length=50)

class Schedule_candstudio(models.Model):
    schedule=models.ForeignKey(Schedule, on_delete=models.CASCADE)
    package=models.ForeignKey(Package, on_delete=models.CASCADE)
    Client=models.ForeignKey(Client, on_delete=models.CASCADE)
