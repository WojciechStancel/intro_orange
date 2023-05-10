from django.shortcuts import render, redirect

from form_app5.models import Task

def create_task_view(request):

    if request.method == "GET":
        return render(
            request,
            'form_app5/task_form.html',
        )
    else:
        task = request.POST.get('task')
        if task:

            #zapis do tabeli Task
            Task.objects.create(name=task)


            #zapis do pliku
            # with open('tasks.txt','a+') as f:
            #     f.write(task + '\n')

        return redirect("form_app5:task_list_view")


def task_list_view(request):

    #odczyt z pliku

    # with open('tasks.txt', 'r') as f:
    #     tasks = f.readlines()

    # odczyt z Tabeli
    tasks = Task.objects.all()

    return render(
        request,
        'form_app5/tasks_list.html',

        context={
            'tasks': tasks,

        }

    )