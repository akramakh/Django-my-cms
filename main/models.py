from django.db import models
from colorfield.fields import ColorField
from faicon.fields import FAIconField

# Create your models here.




class SocialMedia(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    icon = FAIconField()


    def __str__(self):
        return self.name



class Header(models.Model):
    bg_color = ColorField(default='#000000')
    first_sm_account = models.ForeignKey(SocialMedia, on_delete=models.CASCADE, related_name='first_sm_account', null=True)
    second_sm_account = models.ForeignKey(SocialMedia, on_delete=models.CASCADE, related_name='second_sm_account', null=True)
    third_sm_account = models.ForeignKey(SocialMedia, on_delete=models.CASCADE, related_name='third_sm_account', null=True)
    logo = models.ImageField(upload_to="media/images/")

    def __str__(self):
        return "Header"


class Home(models.Model):
    bg_image = models.ImageField(upload_to="media/images/")
    intro_q = models.CharField(max_length=255)
    intro_p = models.TextField()
    intro_btn = models.CharField(max_length=30)

    def __str__(self):
        return "Home Section"



class About(models.Model):
    title = models.CharField(max_length=255)
    personal_image = models.ImageField(upload_to="media/images/")
    username = models.CharField(max_length=255)
    bio = models.TextField()
    resume = models.FileField(upload_to='documents/')
    bg_color = ColorField(default='#000000')

    def __str__(self):
        return "About Section"



class Service(models.Model):
    title = models.CharField(max_length=255)
    intro = models.TextField(null=True)
    bg_color = ColorField(default='#ffffff')

    def __str__(self):
        return "Service Section"



class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    intro = models.TextField(null=True)
    bg_color = ColorField(default='#ffffff')

    def __str__(self):
        return "Portfolio Section"


class Contact(models.Model):
    title = models.CharField(max_length=255)
    intro = models.TextField()
    address = models.CharField(max_length=255, null=True, blank=True, default="my address")
    phone = models.CharField(max_length=255, null=True, blank=True, default="+970590000000")
    email = models.CharField(max_length=255, null=True, blank=True, default="name@domain.com")
    bg_color = ColorField(default='#000000')

    def __str__(self):
        return "Contact Section"



class Footer(models.Model):
    copyright_year = models.CharField(max_length=4, default='2019')
    copyright_for = models.CharField(max_length=100, default="akramakh")
    site_name = models.CharField(max_length=100, default="Portfolio")
    bg_color = ColorField(default='#000000')


    def __str__(self):
        return "Footer"




class FreelanceAccount(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    bg_color = ColorField(default='#000000')


    def __str__(self):
        return self.name




class Message(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    body = models.TextField()


    def __str__(self):
        return self.email

    def full_name(self):
        return self.firstname + ' ' + self.lastname
