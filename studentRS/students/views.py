from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Student

# Create your views here.
def index(request):
  students = Student.objects.all()
  return render(request, "students/index.html", {
     "students": students
  })


def add(request):
  if request.method == "POST":
      name = request.POST.get("name")
      if name is not None:
        student = Student(name = name)
        student.save()
        return HttpResponseRedirect(reverse("index"))
      else:
        return HttpResponse("Name is empty")
  else:
     return render(request, "students/add.html")
