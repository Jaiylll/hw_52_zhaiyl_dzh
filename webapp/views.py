from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.dateparse import parse_date

from webapp.models import Task, status_choices


# Create your views here.
def index(request):
    tasks = Task.objects.order_by("id")
    return render(request, "index.html", context={"tasks": tasks})


def detail(request):
    try:
        task = Task.objects.get(id=request.GET.get("id"))
    except Task.DoesNotExist:
        return HttpResponseRedirect("/")
    return render(request, "task_view.html", context={"task": task})


def create(request):
    if request.method == "GET":
        return render(request, "create_task.html", context={"status_choices": status_choices})
    else:
        description = request.POST.get("description")
        status = request.POST.get("status")
        date_str = request.POST.get("date")
        planned_date = parse_date(date_str) if date_str else None
        Task.objects.create(
            description=description,
            status=status,
            planned_date=planned_date
        )
    return HttpResponseRedirect("/")


def delete(request):
    try:
        task = Task.objects.get(id=request.GET.get("id"))
    except Task.DoesNotExist:
        return HttpResponseRedirect("/")
    task.delete()
    return HttpResponseRedirect("/")
