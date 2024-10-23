from django.shortcuts import render
# from manaliapp.models import MANALI_MODEL
from .forms import manali_form

# Create your views here.
# def manali_view(request):
#     model_list=MANALI_MODEL.objects.all
#     my_dict={'model_list':model_list}
#     return render(request,"manaliapp/manali.html",context=my_dict)

def manali_view(request):
    sent=False
    form = manali_form(request.POST)
    if request.method=='POST':

        if form.is_valid():
            print("DURATION",form.cleaned_data["DURATION"])
            print("HOTELS", form.cleaned_data["HOTELS"])
            print("BUDGET", form.cleaned_data["BUDGET"])
            print("CITIES", form.cleaned_data["CITIES"])
            sent=True

        form=manali_form()
    return render(request,'manaliapp/manali.html',{'form':form,'sent':sent})
