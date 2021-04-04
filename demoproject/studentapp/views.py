from django.shortcuts import render,redirect
from studentapp.models import Student
from django.core.paginator import Paginator

from studentapp.forms import StudentForm,EmailForm
from django.contrib import messages

from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def home(request):
    
    return render(request,"home.html")

def index(request):
    #students=Student.objects.all()
    #students=Student.objects.filter(name__icontains='n')
    #students=Student.objects.filter(name__istartswith='n')
    #students=Student.objects.order_by('name')
    #students=Student.objects.values('name','dob')
    students=Student.objects.order_by('-id')
    paginator=Paginator(students,10)
    page=request.GET.get('page')
    students=paginator.get_page(page)

    context={'title':'Wellcome','students':students}
    return render(request,"student/index.html",context)

def details (request,id):
    student=Student.objects.get(pk=id)
    form=StudentForm(request.POST or None,instance=student)
     
    context={'title':'edit','form':form,"student":student}
    return render(request,"student/details.html",context)



def create(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data inserted successfully')
            return redirect("index")


    else:
        form=StudentForm()
    context={'title':'create','form':form}

    return render(request,"student/create.html",context)


def edit(request,id):
    student=Student.objects.get(pk=id)
    form=StudentForm(request.POST or None,instance=student)
    
           
    context={'title':'edit','form':form,"student":student}

    return render(request,"student/edit.html",context)

def update(request,id):
    student=Student.objects.get(pk=id)
    form=StudentForm(request.POST or None,instance=student)
    
    if form.is_valid():
        form.save()
        messages.success(request,'Data updated successfully')
        return redirect('index')

    context={'title':'edit','form':form,"student":student}
    return render(request,"student/edit.html",context)

def delete(request,id):
    student=Student.objects.get(pk=id)
    student.delete()
    messages.add_message(request,messages.SUCCESS,'Data deleted successfully')
    return redirect('index')


def sendemail(request):
    if request.method=='POST':
        form=EmailForm(request.POST)
        if form.is_valid():
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            email=form.cleaned_data['email']
            try:
                mail=EmailMessage(subject,message,settings.EMAIL_HOST_USER,[email])
                #file attachment code--------Start------------------
                if request.FILES:
                    files=request.FILES.getlist('attach')
                    for f in files:
                        mail.attach(f.name,f.read(),f.content_type)
                #-------------------End-------------------------        
                mail.send()
                messages.error(request,'Email Send Successfully')
                return redirect('index')

            except:
                messages.error(request,'Email Not Send')

    else:
        form=EmailForm()
    
    context={'title':'Email','form':form}
    return render(request,"student/email.html",context)




