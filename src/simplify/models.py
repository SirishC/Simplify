from django.db import models
from .utils import code_generator , create_shortcode
from .validators import validate_url
from django.conf import settings
# Create your models here.

from django.db import models
class  simplifyURL(models.Model):
    url = models.CharField(max_length=220,validators=[validate_url])
    shortcode = models.CharField(max_length=15,unique=True,blank=True)
    def save(self,*args,**kwargs):
        self.shortcode = code_generator()
        print("code generated successfully !" )
        super(simplifyURL,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.url)
    def get_short_url(self):
        # url_path = reverse("scode",kwargs={'shortcode': self.shortcode},host="www")
        return "sirishchejerla:5000/"+self.shortcode
