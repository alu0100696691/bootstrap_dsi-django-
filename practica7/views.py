from django.http import HttpResponse
#from django.template import RequestContext, loader
#from django.shortcuts import render_to_response
from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse

#def homefun(request):
#    return render_to_response('home.html')

def home(request):
	return render(request,"home.html")

def help(request):
        return render(request,"help.html")

def about(request):
        return render(request,"about.html")


#def quick_test(request):
#	return render_to_response("blog.html", {})
