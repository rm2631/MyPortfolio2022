from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from portfolio.models import Project
from django.utils import timezone
# Create your views here.




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 10
    template_name = 'templates/project_list.html'

    def get_queryset(self):
        return Project.objects.all()