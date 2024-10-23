from django.shortcuts import render
# from darjelingapp.models import DARJELING_MODEL
from .forms import darjeling_form
# Create your views here.

# def darjeling_view(request):
#     model_list=DARJELING_MODEL.objects.all
#     my_dict={'model_list':model_list}
#     return render(request,"darjelingapp/darjeling.html",context=my_dict)

def darjeling_view(request):
    sent=False
    form = darjeling_form(request.POST)
    if request.method=='POST':

        if form.is_valid():
            print("DURATION",form.cleaned_data["DURATION"])
            print("HOTELS", form.cleaned_data["HOTELS"])
            print("BUDGET", form.cleaned_data["BUDGET"])
            print("CITIES", form.cleaned_data["CITIES"])
            sent=True

        form=darjeling_form()
    return render(request,'darjelingapp/darjeling.html',{'form':form,'sent':sent})
