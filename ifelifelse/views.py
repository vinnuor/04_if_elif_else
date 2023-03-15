from django.shortcuts import render

# Create your views here.
def if_elif_else(request):
    d={'a':300,'b':200,'c':1000}
    return render(request,'if_elif_else.html',context=d)