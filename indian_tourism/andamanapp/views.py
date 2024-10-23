from lib2to3.fixes.fix_input import context

from django.shortcuts import render
# from andamanapp.models import ANDAMAN_MODEL
from .forms import andaman_form

# Create your views here.
def index_view(request):
    return render(request,"index.html")


# def andaman_view(request):
#     model_list=ANDAMAN_MODEL.objects.all
#     my_dict={'model_list':model_list}
#     return render(request,"andamanapp/andaman.html",context=my_dict)


def andaman_view(request):
    sent=False
    form = andaman_form(request.POST)
    if request.method=='POST':

        if form.is_valid():
            print("DURATION",form.cleaned_data["DURATION"])
            print("HOTELS", form.cleaned_data["HOTELS"])
            print("BUDGET", form.cleaned_data["BUDGET"])
            print("CITIES", form.cleaned_data["CITIES"])
            sent=True

        form=andaman_form()
    return render(request,'andamanapp/andaman.html',{'form':form,'sent':sent})




