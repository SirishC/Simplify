from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View

from .models import simpleURL
# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"Simple/home.html",{})


class SimpleRedirectView(View):
    def get(self,request,shortcode=None,*args,**kwargs):
        obj = get_object_or_404(simpleURL,shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
