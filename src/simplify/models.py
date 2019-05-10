from django.db import models
from .utils import code_generator , create_shortcode
# Create your models here.

class simpleURL(models.Model):
    url         = models.CharField(max_length=220, )
    shortcode   = models.CharField(max_length=15,unique=True,blank=True)
    def save(self,*args,**kwargs):
        self.shortcode = code_generator()
        print("code generated successfully !" )
        super(simpleURL,self).save(*args,**kwargs)


    def __str__(self):
        return str(self.url)
