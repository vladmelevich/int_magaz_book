from django.shortcuts import render
from . import forms
from . import models
def glav(request):
    dan = models.books.objects.all()
    d = {'dan':dan}
    return render(request,'klient/glav.html',d)

def zaks(request):
    if request.method == 'POST':
        form1 = forms.ZakarForm(request.POST)
        if form1.is_valid():
            form1.save()

    form1 = forms.ZakarForm()
    ml = {'form1':form1}
    return render(request, 'klient/zak.html',ml)


def sot(request):
    if request.method == 'POST':
        form = forms.KnigForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    form = forms.KnigForm()

    return render(request, 'sotrud/sotrud.html',{'form':form})

def poisk(request):
    if request.method == 'POST':
        formv = forms.PoiskForm(request.POST)
        if formv.is_valid():
            name = formv.cleaned_data['poisk']
            book_inf = models.books.objects.filter(name__icontains=name).first()
            im = book_inf.im
            har = book_inf.har
            price = book_inf.price

            return render(request, 'sotrud/sotrud1.html',{'name':name,'im':im,'har':har,'price':price})
    formv = forms.PoiskForm()

    return render(request, 'sotrud/sotrud1.html',{'formv':formv})


def zak(request):
    gw = models.za.objects.all()
    return render(request,'sotrud/zak.html',{'gw':gw})
