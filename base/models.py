from django.db import models
from django.contrib.auth.models import  AbstractUser #User,

class User(AbstractUser):
    username = models.CharField(unique = True, max_length=200, 
                                null=False)
    name = models.CharField(null=True, max_length=200)
    bio = models.TextField(null=True)
    creator = models.BooleanField('Creator', default=False)
    completer = models.BooleanField('Completer', default=False) 

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Task(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=200)
    description = models.TextField('Task description', null = False, blank = False) # makle False
    duedate = models.DateField('Duedate (yyyy-mm-dd)')
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
    
class Mark(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    mark = models.BooleanField('Is it completed?', default=False)

    def __str__(self):
        return str(self.mark)