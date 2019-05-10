from django.db import models
from .utils import code_generator , create_shortcode
# Create your models here.
class simpleManager(models.Manager):
    def all(self,*args ,**kwargs):
        qs = super(simpleManager,self).all(*args,**kwargs)
        qs = qs.filter(active=True)
        return qs
    def refresh_code(self):
        qs = simpleURL.objects.filter(id__gte=1)
        code_count = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            code_count +=1
        return "code count is {i}".format(i=code_count)
class simpleURL(models.Model):
    url         = models.CharField(max_length=220, )
    shortcode   = models.CharField(max_length=15,default='abc',unique=True,blank=True)
    active      = models.BooleanField(default=True)
    objects = simpleManager()
    def save(self,*args,**kwargs):
        self.shortcode = code_generator()
        print("code generated successfully !" )
        super(simpleURL,self).save(*args,**kwargs)


    def __str__(self):
        return str(self.url)
