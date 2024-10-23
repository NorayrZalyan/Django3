from django.db import models

# Create your models here.



# Header
class H_Header(models.Model):
    logo_img = models.ImageField('logo' , upload_to='media') 
    company_name = models.CharField('company name' , max_length=30)
    about_the_page = models.CharField(' about the page' , max_length=150)
    img = models.ImageField('page img' , upload_to='media')
    def __str__(self):
        return self.about_the_page
class   H_about_company(models.Model):
    p = models.CharField('title' , max_length=75)
    text = models.TextField('text')
    def __str__(self):
        return self.p
# end header



# WORK
class Work(models.Model):
    work_name = models.CharField('work name' , max_length=100)
    work_about = models.CharField('work about' , max_length=100)
    img = models.ImageField('work img' , upload_to='media')
    OPTION_ONE = 'left'
    OPTION_TWO = 'center'
    OPTION_THREE = 'right'
    CHOICES = [
        (OPTION_ONE, 'left'),
        (OPTION_TWO, 'center'),
        (OPTION_THREE, 'right'),
    ]
    choice_field = models.CharField(max_length=20, choices=CHOICES, default=OPTION_ONE)
    def __str__(self):
        return self.work_name
    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'


# ABOUT
class About(models.Model):
    text = models.TextField('text')
    bgimg = models.ImageField('bg img' , upload_to='media')
    def __str__(self):
        return self.text
class A_link(models.Model):
    name = models.CharField('name' , max_length=50)
    img = models.ImageField('img' , upload_to='media')
    link = models.CharField('link' , max_length=50)
    def __str__(self):
        return self.name




# contact
class contact(models.Model):
    bgimg = models.ImageField('bg img' , upload_to='media')
    adress = models.CharField('adress' , max_length=50)
    email = models.CharField('email' , max_length=50)
    tel = models.CharField('tel' , max_length=50)
    facebook = models.CharField('facebook' , max_length=50)
    instagram = models.CharField('instagram' , max_length=50)
    def __str__(self):
        return self.adress