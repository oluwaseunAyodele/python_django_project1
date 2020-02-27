from django.shortcuts import render
from app_1.models import blogpost,shopProduct

# Create your views here.

def apphome(request):
    context={}
    return render(request,"app_1home.html",context)

def appabout(request):
    context={}
    return render(request,"about.html",context)

def appcontact(request):
    context={}
    return render(request,"contact.html",context)

def appblog(request):
    xcontent=blogpost.objects.all()
    c={"content":xcontent}
    return render(request,"blog.html", c)

def appblog_details(request,cid ):
    xc=blogpost.objects.get(id=cid)
    q={"xc":xc}
    return render(request,"blog_details.html",q)
#appabout,appblog, appcontact


def shop(request ):
    #xc=blogpost.objects.get(id=cid)
    #q={"xc":xc}
   
    itms=shopProduct.objects.all()
    q={"itms":itms}
    return render(request,"shop.html",q)

  






