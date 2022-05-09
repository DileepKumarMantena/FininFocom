from django.db import models

# Create your models here.

Country = (
    ('India', 'India'),
    ('Usa', 'Usa'),
    ('England', 'England')

)


class UserModel(models.Model):
    class Gender(models.TextChoices):
        Male = 'Male'
        Female = 'Female'

    Name = models.CharField(max_length=250)
    DOB = models.DateTimeField()
    EmailId = models.EmailField(max_length=254)
    PhoneNumber = models.CharField(max_length=12)
    Gender = models.CharField(max_length=10, choices=Gender.choices)

    FlatNo = models.CharField(max_length=250)
    Street = models.CharField(max_length=250)
    Country = models.CharField(max_length=100, choices=Country, default='India')
    PhotoUpload = models.ImageField()

    class Meta:
        db_table = "Registration_Table"
