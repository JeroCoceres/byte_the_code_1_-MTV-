from django.db import models
from django.contrib.auth.models import User
from admin_settings.models import Country,Language

class UserProfile(models.Model):
    CHOICE = (
        ("full-time","full-time"),
        ("part-time","part-time"),
        ("freelance","freelance"),
        ("other","other")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    profile_image = models.ImageField(upload_to="profile_images",blank=True,null=True)
    cover_image = models.ImageField(upload_to="cover_images",blank=True,null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500,blank=True,null=True)
    availability = models.CharField(max_length=30,choices=CHOICE,blank=True,null=True)
    birth_date = models.DateField(blank=True,null=True)
    years_of_experience = models.PositiveIntegerField(blank=True,null=True)
    address = models.CharField(max_length=150,blank=True,null=True)
    company_name = models.CharField(max_length=100,blank=True,null=True)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT, blank=True,null=True)
    language = models.ForeignKey(Language, on_delete=models.RESTRICT, blank=True,null=True)


    def __str__(self):
        return self.user.username
    