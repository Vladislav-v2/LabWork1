from django.db import models

# Create your models here.
class Example(models.Model):
    integer_field = models.IntegerField()
    positive_field = models.PositiveIntegerField(),
    positive_small_field = models.PositiveSmallIntegerField()
    big_integer_fiels = models.BigIntegerField()
    float_feils = models.FloatField()
    bitary_feild = models.BinaryField()
    boolean_feild = models.BooleanField()
    char_feild = models.CharField(max_length=5)
    text_feild = models.TextField(max_length=20)
    date_field = models.DateField(auto_now= False)
    datre_time_fiels = models.DateTimeField(auto_now_add=False)
    decimal_feild = models.DecimalField(max_digits=8,decimal_places=2)
    email_feils = models.EmailField()
    file_feild = models.FileField()
    image_feild = models.ImageField()

class Author(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    birthday= models.DateField(auto_now=False)
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автори"
    def __str__(self):
        return "Назва : %s Автор : %s" %(self.name, self.surname)

class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=50)
    about = models.TextField(max_length=1000)
    genre_list = (
        (("f","fetnesy"),
         ( "h","horror"),
        ( "d","detetive"),
        ("c","comedy"),
        ("b","biograhpi"))
        )
    genre = models.CharField(max_length=50, choices=genre_list)
    def __str__(self):
        return "Назва : %s" % self.name
class Place(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    def __str__(self):
        return "Місце : %s" % self.adress

class Restaurant(models.Model):
    place = models.OneToOneField(Place,on_delete=models.CASCADE,primary_key=True)
    home_delivery = models.BooleanField(default=False)
    round_the_clock = models.BooleanField(default=False)
    def __str__(self):
        return "Ресторан : %s" % self.place

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=50)
    def __srt__(self):
        return "Ім'я офіціанта: %s,Ресторан: %s" %(self.name, self.restaurant)

class Publication(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return "Назва: %s" %self.name

class Article(models.Model):
    name = models.CharField(max_length=50)
    publications = models.ManyToManyField(Publication)
    def __str__(self):
        return "Назва: %s" %self.name
