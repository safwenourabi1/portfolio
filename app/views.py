from django.shortcuts import render
from .models import contact



# Create your views here.





def main(request):
    if request.method == 'POST':
        
        name= request.POST['name']
        email= request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        contact.objects.create(
             name=name,
             email=email,
             subject=subject,
             message=message,

         
            )
        
    return render(request,'index.html')
def show1(request):
    return render(request,'project samm.html')
def show2(request):
    return render(request,'Database.html')
def show3(request):
    return render(request,'imageencryptionproject.html')
def show4(request):
    return render(request,'electronicproject.html')