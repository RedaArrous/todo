from django.db import models
from django.contrib.auth.models import User

# Create your models here.

IMPORTANCE_CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
]


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos', verbose_name="owner")
    title = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=50, blank=True)
    importancy = models.CharField(max_length=50, blank=True, choices= IMPORTANCE_CHOICES, default="Low")
    date_added = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
    class Meta:
        ordering = ['-date_added']

    
    

