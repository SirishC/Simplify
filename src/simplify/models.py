from django.db import models
from .utils import code_generator , create_shortcode
from .validators import validate_url
from django.conf import settings
from django_hosts.resolvers import reverse

SHORTCODE_MAX = getattr(settings,"SHORTCODE_MAX" , 15)
# Create your models here.
class simpleManager(models.Manager):
    def all(self,*args ,**kwargs):
        qs = super(simpleManager,self).all(*args,**kwargs)
        qs = qs.filter(active=True)
        return qs
    def refresh_code(self):
        qs = simpleURL.objects.filter(id__gte=1)
        code_count = 1
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            code_count +=1
        return "code count is {i}".format(i=code_count)


class simpleURL(models.Model):
    url         = models.CharField(max_length=220,validators=[validate_url])
    shortcode   = models.CharField(max_length=SHORTCODE_MAX,unique=True,blank=True)
    active      = models.BooleanField(default=True)
    objects = simpleManager()
    def save(self,*args,**kwargs):
        self.shortcode = code_generator()
        print("code generated successfully !" )
        super(simpleURL,self).save(*args,**kwargs)
    def __str__(self):
        return str(self.url)


    def get_short_url(self):
        # url_path = reverse("scode",kwargs={'shortcode': self.shortcode},host="www")
        return "sirishchejerla:5000/"+self.shortcode


# from django.db import models
# class  simpleURL(models.Model):
#     url = models.CharField(max_length=220,)
#     def __str__(self):
#         return str(self.url)
