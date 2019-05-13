from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View

from .forms import submitURL
from .models import simplifyURL
# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kwargs):
        the_form = submitURL()
        context={
            'title' : 'Submit URL' ,
            'form' : the_form,
        }
        return render(request,"simplify/home.html",context)


    def post(self,request,*args,**kwargs):
        form = submitURL(request.POST)
        context={
            'title' : 'Submit URL' ,
            'form' : form,
        }
        template = "simplify/home.html"
        if form.is_valid():
            obj, create = simplifyURL.objects.get_or_create(url=form.cleaned_data.get("url"))
            context = {
            'object':obj,
            'create':create
            }
            if(create):
                template = "simplify/success.html"
            else:
                template = "simplify/already_exist.html"
        return render(request,template,context)

class SimpleRedirectView(View):
    def get(self,request,shortcode=None,*args,**kwargs):
        obj = get_object_or_404(simplifyURL,shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
