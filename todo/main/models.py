from tabnanny import verbose
from django.db import models

# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=100)    # название задачи
    author = models.CharField(max_length=50)    # автор задачи
    description = models.TextField()            # описание задачи
    deadline = models.DateField()               # дедлайн задачи (время выполнения)
    importance = models.IntegerField(help_text="There are 3 levels of importance: 1, 2, 3. 1 is the most important.")  
                                                # важность задачи 
    completed = models.BooleanField(default=False) # выполнена ли задача
    # ------------------- Даты создания и обновления -------------------
    created_at = models.DateTimeField(auto_now_add=True) # дата создания задачи
    updated_at = models.DateTimeField(auto_now=True)     # дата последнего обновления задачи
    # ------------------- Дополнительные поля -------------------
    color = models.CharField(max_length=20, default="#007bff", help_text="цвет текста") # цвет текста
    background_color = models.CharField(max_length=20, default="#f8f9fa", help_text="цвет фона") # 
    
    
    def __str__(self):
        return f'{self.author.upper()}. Deadline: {self.deadline}. Importance: {self.importance}. Completed: {self.completed}'
    
    class Meta:
        verbose_name = "ToDo"
        verbose_name_plural = "ToDos"