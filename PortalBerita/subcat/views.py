from django.shortcuts import render, get_object_or_404, redirect
from .models import SubCat
from cat.models import Cat

# Create your views here.
###---#---### Sub Category List Function For Back (Admin Panel - Backend) Start ####--#--####
def subcat_list(request):
    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End
    subcat = SubCat.objects.all()
    return render(request, 'back/subcat_list.html', {'subcat':subcat})
###--#--### Sub Category List Function For Back (Admin Panel - Backend) End ####--#--####


###--#--### Sub Category Add Function For Back (Admin Panel - Backend) Start ###--#--###
def subcat_add(request):
    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End
    cat = Cat.objects.all()   # for dynamic category. cat object used for an query.
    if request.method == 'POST':
        name = request.POST.get('name')  # name is the field name
        catid = request.POST.get('cat')  # cat is the name of field in html file
        if name == "" :
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})
        #### Check category exist or not Start ####
        if len(SubCat.objects.filter(name=name)) != 0:     # if 1 means exist
            error = "This Name Used Before"
            return render(request, 'back/error.html', {'error':error})
        #### Check category exist or not End ####
        #### By deafult set category Start ####
        catname = Cat.objects.get(pk=catid).name
        b = SubCat(name=name, catname=catname, catid=catid)  # from models.py file, we can get this field name
        b.save()
        return redirect('subcat_list')   # subcat_list function
        #### By deafult set category End ####
    ## {'cat':cat}, for dynamic category.This cat query will be used in subcat_add.html file for dynamic.
    return render(request, 'back/subcat_add.html', {'cat':cat})
###--#--### Sub Category Add Function For Back (Admin Panel - Backend) End ###--#--###

###--#--### Sub Category Edit Function For Back (Admin Panel - Backend) Start ###--#--###
def subcat_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('mylogin')
    subcat = get_object_or_404(SubCat, pk=pk)
    cat = Cat.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        catid = request.POST.get('cat')
        if not name or not catid:
            error = "All fields are required"
            return render(request, 'back/error.html', {'error': error})
        # Cek duplikat nama subcat (kecuali dirinya sendiri)
        if SubCat.objects.exclude(pk=pk).filter(name=name).exists():
            error = "This name is already used by another subcategory"
            return render(request, 'back/error.html', {'error': error})
        catname = Cat.objects.get(pk=catid).name
        subcat.name = name
        subcat.catid = catid
        subcat.catname = catname
        subcat.save()
        return redirect('subcat_list')
    return render(request, 'back/subcat_edit.html', {'subcat': subcat, 'cat': cat})
###--#--### Sub Category Edit Function For Back (Admin Panel - Backend) End ###--#--###

###--#--### Sub Category Del Function For Back (Admin Panel - Backend) Start ###--#--###
def subcat_del(request, pk):
    if not request.user.is_authenticated:
        return redirect('mylogin')
    subcat = get_object_or_404(SubCat, pk=pk)
    subcat.delete()
    return redirect('subcat_list')
###--#--### Sub Category Del Function For Back (Admin Panel - Backend) End ###--#--###