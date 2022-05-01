from django.db import models

# Create your models here.
class Tag(models.Model):
    tech_tag = models.CharField(max_length=64)

    def __str__(self):
        return self.tech_tag


class Project(models.Model):
    project_name = models.CharField(max_length=128)
    tech_tags = models.ManyToManyField(Tag)
    github_url = models.CharField(max_length=256)
    project_description = models.CharField(max_length=512)
    
    def __str__(self):
        return self.project_name

