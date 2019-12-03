from django.shortcuts import render,HttpResponse


def home_page(request):
    return render(request,"home_page.html",{})

def hakkimda_page(request):
    return render(request,'hakkimda.html',{})
def contact_page(request):
    return render(request,'iletisim.html',{})