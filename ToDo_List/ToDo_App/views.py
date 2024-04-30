from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
 

# Create your views here.
def ToDo(request):
    return render(request,'ToDo_List.html')

def home(request):
    Tasks = Task.objects.all()
    context = {}
    context['Tasks']=Tasks
    return render(request,'ToDo.html',context)

def complete(request):
    Tasks = Task.objects.filter(complete=True)
    context = {}
    context['Tasks']=Tasks
    return render(request,'complete.html',context)

def pending(request):
    Tasks = Task.objects.filter(complete=False)
    context = {}
    context['Tasks']=Tasks
    return render(request,'pending.html',context)

def createToDo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        time = request.POST.get('time')
        complete =False

        if title != "" and date !="" and time != "":
            task = Task(
                title=title,
                describtion = desc,
                date = date,
                time = time,
                complete =complete
            ) 
            task.save()
            return redirect('home')
    else:
        return render(request,'createToDo.html')
        
    return render(request,'createToDo.html')

def delete(request,task_id):
    tasks = Task.objects.get(id=task_id)
    context = {}
    context['tasks']=tasks
    return render(request,'delete.html',context)


def task_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.complete = not task.complete
        task.save()
        referring_url = request.META.get('HTTP_REFERER')
        if referring_url is None or referring_url == '':
            return redirect('home')
        return redirect(referring_url)

def task_delete(request,task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.delete()
        referring_url = request.META.get('HTTP_REFERER')
        if referring_url is None or referring_url == '':
            return redirect('home')
        return redirect(referring_url)
    

