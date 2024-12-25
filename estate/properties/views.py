from django.shortcuts import render,get_object_or_404
from .models import Properties,Commentt
from .forms import Comment
from django.contrib import messages
# Create your views here.
def properties(request,**kwargs):
   
    properties = Properties.objects.all()
    context = {
        'properties':properties
    }
    return render(request,'properties/properties.html',context=context)


def properties_detail(request,id):
    form = Comment()
    properties = get_object_or_404(Properties,id=id)
    comments = Commentt.objects.filter(properties=properties.id)
  
    context = {
        'properties':properties,
        'form':form,
        'comments':comments
    }
    if request.method == 'POST':
        form = Comment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.properties = properties
            comment.save()
            messages.add_message(request,messages.SUCCESS,'ok')
            return render(request,'properties/property-single.html')
        else:
            messages.add_message(request,messages.ERROR,'not ok')
            return render(request,'properties/property-single.html')



    else:

        return render(request,'properties/property-single.html',context=context)
