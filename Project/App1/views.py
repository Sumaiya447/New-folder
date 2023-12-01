from django.shortcuts import render,HttpResponse,redirect
from . models import*

# Create your views here.
def homePage(request):
    emp = employee.objects.all()
    return render(request,'home.html',{'emp':emp})


def addEmp(request):
    if request.method == "POST":
        eName = request.POST.get('Name')
        eEmail = request.POST.get('Email')
        eAddress = request.POST.get('Address')
        ePhone = request.POST.get('Phone')
        eSalary = request.POST.get('Salary')

        EMP = employee(name=eName,email=eEmail,address=eAddress,phone=ePhone,salary=eSalary)
        EMP.save()
        return redirect('home')
    

def editEmp(request):
    emp = employee.objects.all()
    return render(request,'home.html',{'emp':emp})


def updateEmp(request,id):
     if request.method == "POST":
        eName = request.POST.get('Name')
        eEmail = request.POST.get('Email')
        eAddress = request.POST.get('Address')
        ePhone = request.POST.get('Phone')
        eSalary = request.POST.get('Salary')

        updateEMP = employee(
            id=id,
            name=eName,
            email=eEmail,
            address=eAddress,
            phone=ePhone,
            salary=eSalary)
        
        updateEMP.save()
        return redirect('home')
     return render (request,'home.html')

def deleteEmp(request,id):
    emp = employee.objects.filter(id=id)
    emp.delete()
    return redirect('home')
        