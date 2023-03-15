from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.core.paginator import Paginator
def index(request):
    item_list= Item.objects.all()
    #context ={ 
     #   'item_list':item_list,
    #}
    food_name=request.GET.get('food_name')
    if food_name!='' and food_name is not None:
        item_list=item_list.filter(item_name__icontains=food_name)
        
    paginator=Paginator(item_list,2)
    page=request.GET.get('page')
    item_list=paginator.get_page(page)
    
    return render(request,'food/index.html',{'item_list':item_list})


def detail(request,id):
    item=Item.objects.get(pk=id)
    context ={
        'item':item,
    }    
    return render(request,'food/detail.html',context)

def create_item(request):
    form=ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form})

def update_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form,'item':item})

def delete_item(request,id):
    item=Item.objects.get(id=id)
    
    if request.method=='POST':
        item.delete()
        return redirect('food:index')
    
    return render(request,'food/item-delete.html',{'item':item})


# Create your views here.