from django.shortcuts import render,redirect
from .models import Upload
from django.http import HttpResponse

# Create your views here.


def Display_All(request):
    obj=Upload.objects.all().order_by('id')
    context={
        'obj':obj,
    }
    return render(request,"index.html",context)

def Display_Images(request,slug):
    try:
        img=Upload.objects.filter(name=slug)
   
        context={
            'img':img[0],

        }
        return render(request,"imgview.html",context)
    except:
        return redirect("Display_All")
        

def about(request):
    obj=Upload.objects.all()
    context={
        'obj':obj,
    }
    return render(request,"about.html",context)
    # return redirect("Display_All")
def View_images(request):
    return redirect("Display_All")
def users(request):
    return redirect("Display_All")

def error_400(request, exception):
    return render(request,"error.html",{'error':"400 Bad Request","mesg":"Your browser sent a request that this server could not understand."})

def error_403(request, exception):
    return render(request,"error.html",{'error':'403 Forbidden',"mesg":" The page or resource you were trying to reach is absolutely forbidden for some reason."})

def error_404(request, exception):
    return render(request,"error.html",{'error':'404 Page Not Found',"mesg":"The requested URL was not found on this server."})

def error_500(request):
    return render(request,"error.html",{'error':'500 Server Error',"mesg":"The server encountered an internal error or misconfiguration and was unable to complete your request."})