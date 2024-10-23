from django.shortcuts import render
# from kerelaapp.models import KERELA_MODEL
from.forms import kerela_form

# Create your views here.
# def kerela_view(request):
#     model_list=KERELA_MODEL.objects.all
#     my_dict={'model_list':model_list}
#     return render(request,"kerelapp/kerela.html",context=my_dict)


def kerela_view(request):
    sent=False
    form = kerela_form(request.POST)
    if request.method=='POST':

        if form.is_valid():
            print("DURATION",form.cleaned_data["DURATION"])
            print("HOTELS", form.cleaned_data["HOTELS"])
            print("BUDGET", form.cleaned_data["BUDGET"])
            print("CITIES", form.cleaned_data["CITIES"])
            sent=True

        form=kerela_form()
    return render(request,'kerelapp/kerela.html',{'form':form,'sent':sent})

