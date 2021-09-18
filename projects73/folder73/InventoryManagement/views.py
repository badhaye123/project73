from django.shortcuts import render,redirect
from .forms import ProductModelForm
from .models import Product

# Create your views here.

def testView(request):
    template_name = 'base.html'
    context = {}
    return render(request,template_name,context)


def homeView(request):
    template_name = 'home.html'
    context = {}
    return render(request,template_name,context)


def addOrderView(request):
    form = ProductModelForm()    
    if request.method =='POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showorder')
    template_name ='addOrder.html'
    context = {'form':form}
    return render(request,template_name,context)


def showOrderView(request):
    pro = Product.objects.all()
    print(pro)
    template_name = 'showOrder.html'
    context = {'pro':pro}
    return render(request,template_name,context)


def updateOrderView(request,pk):
    pro = Product.objects.get(id=pk)
    form = ProductModelForm(instance=pro)
    if request.method == 'POST':
        form = ProductModelForm(request.POST,instance=pro)    
        if form.is_valid():
            form.save()
            print('data updated')
            return redirect('showorder')
    template_name = 'addOrder.html'
    context = {'form':form}
    return render(request,template_name,context)
    

def deleteOrderView(request,pk):
    pro = Product.objects.get(id=pk)
    pro.delete()
    print('data deleted')
    return redirect('showorder') 

