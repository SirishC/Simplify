from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View

from .forms import submitURL
from .models import simpleURL
# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kwargs):
        the_form = submitURL()
        context={
            'title' : 'Submit URL' ,
            'form' : the_form,
        }
        return render(request,"Simple/home.html",context)


    def post(self,request,*args,**kwargs):
        form = submitURL(request.POST)
        context={
            'title' : 'Submit URL' ,
            'form' : form,
        }
        template = "Simple/home.html"
        if form.is_valid():
            obj, create = simpleURL.objects.get_or_create(url=form.cleaned_data.get("url"))
            context = {
            'object':obj,
            'create':create
            }
            if(create):
                template = "Simple/success.html"
            else:
                template = "Simple/already_exist.html"
        return render(request,template,context)

class SimpleRedirectView(View):
    def get(self,request,shortcode=None,*args,**kwargs):
        obj = get_object_or_404(simpleURL,shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
