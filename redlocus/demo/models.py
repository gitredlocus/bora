from django.db import models

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    group_name   = models.CharField(max_length=50)
    trend   = models.SmallIntegerField()

    def __unicode__(self):
        return self.project_name
