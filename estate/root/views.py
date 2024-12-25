from django.shortcuts import render
from .models import Agent,Tester,contactus
from .forms import Contactusform
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'root/index.html')

def agent(request):
    agents = Agent.objects.filter(status=True)
    context = {
        'agents':agents
    }
    return render(request,'root/agents.html',context=context)


#def contact(request):
  #  if request.method == 'POST':
  #      form = Contactusform(request.POST)
  #      if form.is_valid():
  #          contact = contactus()
 #           contact.name = request.POST.get('name')
  #           contact.subject = request.POST.get('subject')
 #           contact.message = request.POST.get('message')
   #         contact.save()
   #         messages.add_message(request,messages.SUCCESS,'true')
   #         return render(request,'root/contact.html')
 #       else:
 #           messages.add_message(request,messages.ERROR,'false')
 #           return render(request,'root/contact.html')
 #   else:
  #      return render(request,'root/contact.html')

def contact(request):
    if request.method == 'POST':
        form = Contactusform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'true')
            return render(request,'root/contact.html')
        else:
            messages.add_message(request,messages.ERROR,'false')
            return render(request,'root/contact.html')
    else:
        form = Contactusform()
        context = {'form':form}
        return render(request,'root/contact.html',context=context)


def about(request):
    return render(request,'root/about.html')
