from django.shortcuts import render, redirect
from django.db.models import Count
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import *
import json

class EmployeeView(View):
    def get(self, request):
        employ = Employee.objects.all().order_by("hire")
        return render(request, "employee.html", {"employee": employ, "count": employ.count()})

class PositionView(View):
    def get(self, request):
        return render(request, "position.html", {"position": Position.objects.annotate(pos_employ = Count("employee")).order_by("id")})

class ProjectView(View):
    def get(self, request):
        return render(request, "project.html", {"project": Project.objects.all()})
    def delete(self, request, project_id):
        dele = Project.objects.get(id = project_id)
        dele.delete()
        return HttpResponse(project_id)

class ProjectEditView(View):
    def get(self, request, project_id):
        proj = Project.objects.get(id = project_id)
        return render(request, "project_detail.html", {
            "proj": proj,
            "start" : proj.start.strftime('%Y-%m-%d'),
            "due" : proj.due.strftime('%Y-%m-%d'),
            "member" : proj.staff.all()
        })
    def put(self, request, project_id):
        em_id = json.loads(request.body).get('emp_id')
        project = Project.objects.get(id = project_id)
        emp = Employee.objects.get(id = em_id)
        add = project.staff.add(emp)
        return HttpResponse(project_id)
    def delete(self, request, project_id, employee_id):
        project = Project.objects.get(id = project_id)
        emp = Employee.objects.get(id = employee_id)
        project.staff.remove(emp)
        return JsonResponse({'foo':'bar'}, status=200)

def layout(request):
    return render(request, "layout.html")
