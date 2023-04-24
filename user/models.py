from django.db import models

# Create your models here.
class slider(models.Model):
    image1=models.ImageField(upload_to='Slider', blank=True)
    image2=models.ImageField(upload_to='Slider', blank=True)
   
    title=models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.title
    
class About(models.Model):
    title=models.CharField(max_length=255, unique=True)
    content=models.TextField(max_length=500,blank=True)
    image=models.ImageField(upload_to='About', blank=True)
    def __str__(self):
        return self.title
    
# class Contact(models.Model):
#     number=models.IntegerField()
#     def __str__(self):
#         return self.name
    
class digitalmarketingservice(models.Model):
    title=models.CharField(max_length=250,unique=True) 
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='digital',blank=True)
    def __str__(self):
        return self.title
    
class webdevelopmentservice(models.Model):
    title=models.CharField(max_length=250,unique=True) 
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='web',blank=True)
    def __str__(self):
        return self.title 
    
class graphicdesigning(models.Model):
    title=models.CharField(max_length=250,unique=True) 
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='web',blank=True)
    def __str__(self):
        return self.title         
        
class Gallery(models.Model):
     image=models.ImageField(upload_to='Gallery', blank=True)
    # def __str__(self):
         # return self.image
    
class galleryaccola(models.Model):
    imageacc=models.ImageField(upload_to='Gallery', blank=True)
     

# class Contact(models.Model):
#     name=models.CharField(max_length=150)
#     email=models.EmailField()
#     phonenumber=models.IntegerField()
#     message=models.TextField()
#     def __str__(self):
#         return self.name

# class client(models.Model):
#     name=models.CharField(max_length=100,unique=True)
#     email=models.EmailField()
#     number=models.CharField(max_length=100,null=True)
#     message=models.TextField()
#     def __str__(self):
#         return self.name
    
class Clients(models.Model):
    name=models.CharField(max_length=100,unique=True)
    email=models.EmailField()
    number=models.CharField(max_length=100,null=True)
    message=models.TextField()
    def __str__(self):
            return self.name  