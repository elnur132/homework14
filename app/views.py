from django.shortcuts import render,redirect, get_object_or_404
from .models import Task
# Create your views here.
def show_task(request):
    tasks = Task.objects.all()
    return render(request, 'show_task.html', {'tasks':tasks})

def add_task(request):
    if request.method == 'POST':
        task = request.POST
        add = Task.objects.create(name=task['name'], description=task['description'])
        add.save()
        return redirect('show-tasks')
    else:
        return render(request, 'add-tasks.html')

def update_task(request, id):
    try:
        task = get_object_or_404(Task, id=id)
        if request.method == 'POST':
            updated_task = request.POST
            task.name = updated_task['name']
            task.description = updated_task['description']
            task.save()
            return redirect('show-tasks')
        else:
            return render(request, 'update-tasks.html', {'task':task})
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Task doesn't exist</h2>")

def delete_task(request, id):
    try:
        task = get_object_or_404(Task, id=id)
        task.delete()
        return redirect('show-tasks')
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Task doesn't exist</h2>")