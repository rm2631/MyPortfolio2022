from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=128)
    github_url = models.CharField(max_length=256)
    github_readme = models.CharField(max_length=256)
    
    def __str__(self):
        return self.project_name
