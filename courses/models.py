from django.db import models

# Create your models here.
class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    '''con el anterior còdigo decimos que la fecha es autogenrada
    cuando creamos los registros
    '''
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    '''TextField es para grandes cantidades de texto
    '''
    def __str__(self):
        return self.title

class Lesson (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True, default='')
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    '''
    Curse, on_delete=models.CASCADE => cuando se borra un curso,
    se borraran todas las lecciones que pertenezcan a este
    '''

    #def __str__(self):
     #   return self.title

    class Meta:
        ordering = ['order',]
    def __str__(self):
        return self.title