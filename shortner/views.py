from django.http.response import HttpResponse
from shortner.models import links
from django.shortcuts import redirect, render
import uuid


# Create your views here.
def index(request):
          
          return render(request,"index.html",{})

def shortit(request):
          if request .method=="POST":
                    link = request.POST["url"]
                    uid = str(uuid.uuid4())[:5]
                    urllink =links(url=link,uuid=uid)
                    urllink.save()
          return HttpResponse(uid)

def redshort(request,short):
          
          try:
                    surl = links.objects.get(uuid=short)
                    return redirect(surl.url)
          except:
                    return redirect("/")
          
