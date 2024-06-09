from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, request
from django.shortcuts import render, redirect

from taskapp.models import Task, Department


# Create your views here.
def home(request):
    data={"login":True,"sign":True}
    # return render (request,'index.html')
    return render(request,'signin.html',data)


def signin_fun(request):
    if request.method=="POST":
        name=request.POST["txtname"]
        email=request.POST["txtemail"]
        password=request.POST["txtpswd"]
        #checking user details
        if User.objects.filter(Q(username=name)|Q(email=email)).exists():
            # data={"msg""True"}
            data = {"login": False, "sign": True}

            return render(request,'signin.html',data)
        else:
             # creating superuser directly
            u1=User.objects.create_superuser(username=name,email=email,password=password)
            u1.save()
            data = {"login": True, "sign": False}

            return render(request,'signin.html',data)
    data = {"login": False, "sign": True}
    return render(request,'signin.html',data)



def login_fun(request):
    if request.method=="POST":
        name=request.POST["name"]
        password=request.POST["pswd"]
        # authenticate checks both username & password,if its wrong means it returns none.
        user=authenticate(username=name,password=password)
        if user is not None:
            if user.is_superuser:
                return render(request,'dashboard.html')
            else:
                # data={"msg":True}
                data = {"login": True, "sign": False}
                return render(request,'signin.html',data)
        else:
            # data={"msg":True}
            data = {"login": True, "sign": False}
            return render(request,'signin.html',data)
    data = {"login": True, "sign": False}
    return render(request,'signin.html',data)


def display_fun(request):
    # task is a model name(table name)
    data = Task.objects.all()
    return render(request,'dashboard.html',{"tasks":data,"display":True})

def add_fun(request):
    department=Department.objects.all()
    if request.method=="POST":
        t1=Task()
        t1.task_created=request.POST["tskdate"]
        t1.name=request.POST["nametxt"]
        department_id=request.POST.get('dept1')
        department_instance=Department.objects.get(pk=department_id)
        t1.dept=department_instance
        t1.task=request.POST["task"]
        t1.status=request.POST["task"]
        t1.save()
        return redirect('display')
    else:
        return render(request,'dashboard.html',{"display":False,"department":department,"add":True})


def log_fun(request):
    data={"login":True,"sign":True}
    return redirect("home")
    # return render (request,'signin.html',data)


def update_fun(request,id):
    tasks=Task.objects.get(id=id)
    department=Department.objects.all()
    if request.method=="GET":
        data={"tasks":tasks,"department":department,"display":False,"add":True}
        return render(request,'dashboard.html',data)
    else:
        data={"tasks":tasks,"department":department,"display":False,"add":True}
        try:
            tasks.task_created=request.POST['tskdate']
            tasks.name=request.POST['nametxt']
            department_id=request.POST.get('dept1')
            department_instance=Department.objects.get(pk=department_id)
            tasks.dept=department_instance
            tasks.task=request.POST['task']
            tasks.status=request.POST['status']
            tasks.save()
        except:
            return render(request,'dashboard.html',data)
        
        return redirect("display")
    # return HttpResponse("welcome")



def delete_fun(request,id):
    task1=Task.objects.get(id=id)
    task1.delete()
    return redirect("display")