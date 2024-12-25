from django.shortcuts import render,get_object_or_404,redirect
from .models import Service,Comment
from .forms import Commentform
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.
def service(request,**kwargs):
    if kwargs.get('categorys') :
        service = Service.objects.filter(cat__name=kwargs.get('categorys'))
      
    elif request.GET.get('search'):
        search = request.GET.get('search')
        service = Service.objects.filter(name__contains=search)
      

    else:
        service = Service.objects.all()
       
    
    service_pageinate = Paginator(service,2)
    first_page = 1
    last_page = service_pageinate.num_pages

    try:
        page_number = request.GET.get("page")
        service = service_pageinate.get_page(page_number)
    except:
        page_number = first_page
        service = service_pageinate.get_page(first_page)

    context = {
        'services':service,
        'last':last_page,
        'first':first_page,
    }
    return render(request,'service/services.html',context=context)

def service_detail(request,id):
    form = Commentform()
    service = Service.objects.filter(status=True,service=service.id)
    service = get_object_or_404(Service,id=id)
    context = {
        'services':service,
        'form':form,
        'service':service
    }
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = Commentform(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.service = service
                comment.save()
                messages.add_message(request,messages.SUCCESS,'ok')
                return render(request,'service/service-details.html',context=context)
            else:
                messages.add_message(request,messages.ERROR,'not ok')
                return render(request,'service/service-details.html',context=context)
        else:
            return redirect('accounts:login')


    else:
        return render(request,'service/service-details.html',context=context)