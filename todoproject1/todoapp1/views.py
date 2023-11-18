from django.urls import reverse_lazy
from . models import Task
from django.shortcuts import redirect, render
from . forms import TodoForm

from django.views.generic  import ListView
from django.views.generic.detail  import DetailView
from django.views.generic.edit import UpdateView,DeleteView



#create your class based views
class TaskListview(ListView):
    model:Task
    template_name = 'index.html'
    context_object_name = 'task1'
    def get_queryset(self):
        # Return a custom queryset or any logic to fetch the data
        return Task.objects.all()  # For example, fetch all Task objects


class TaskDetailview(DetailView):
    model:Task
    template_name = 'details.html'
    context_object_name = 'task1'
    def get_queryset(self):
        # Return a custom queryset or any logic to fetch the data
        return Task.objects.all()  # For example, fetch all Task objects



class TaskUpdateview(UpdateView):
    model:Task
    template_name = 'Update.html'
    context_object_name = 'task1'
    fields=['name','priority','date']
    def get_queryset(self):
        # Return a custom queryset or any logic to fetch the data
        return Task.objects.all()  # For example, fetch all Task objects
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})



class TaskDeleteview(DeleteView):
    model:Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
    def get_queryset(self):
        # Return a custom queryset or any logic to fetch the data
        return Task.objects.all()  # For example, fetch all Task objects


# Create your function  views here.

def add_task(request):
    task1=Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task = Task(name=name, priority=priority,date=date)
        try:
            print('task saved')
            task.save()
            
        except Exception as e:
            print('error while saving')
            pass
    return render(request, 'index.html',{'task1':task1})



def details(request):
    task2 = Task.objects.all()
    return render(request,'details.html',{'task2':task2})

def delete(request,taskid):
    task3=Task.objects.get(id=taskid)
    if request.method == 'POST':
        task3.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task4 = Task.objects.get(id=id)
    f = TodoForm(request.POST or None,instance = task4)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task4':task4})
    