from django.db import models

# Create your models here.
class Human(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth = models.DateField()
    company_list = (
        ("Epam", "Epam"),
        ("Microsoft", "Microsoft"),
        ("Apple", "Apple"),
        ("IBM", "IBM"),
        ("Ubisoft", "Ubisoft")
    )
    company = models.CharField(max_length=150, choices=company_list)
    position_list = (
        ("frontEnd-developer", "frontEnd-developer"),
        ("backEnd-developer", "backEnd-developer"),
        ("JavaScript-develoter", "JavaScript-develoter")
    )
    position = models.CharField(max_length=15, choices=position_list)
    language_list = (
        ("C++", "C++"),
        ("C-sharp", "C-sharp"),
        ("JavaScript", "JavaScript"),
        ("Python", "Python"),
        ("Java", "Java"),
    )
    language = models.CharField(max_length=10, choices=language_list, default=language_list[1])
    salary = models.IntegerField()
    def __str__(self):
        return " %s %s: %s" %(self.surname, self.name, self.company)