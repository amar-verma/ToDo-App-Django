from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=25)
    describtion = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    complete = models.BooleanField(default=False)    

    def __str__(self):
        return self.title

    # def __str__(self) -> str:
    #     return f'{self.title}'
