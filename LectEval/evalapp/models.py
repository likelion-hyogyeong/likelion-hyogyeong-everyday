from django.db import models
from datetime import datetime
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now,blank=True)
    completion = (
        ('이수영역 선택','이수영역 선택'),
        ('전공', '전공'),
        ('교양', '교양'),
        ('선택', '선택'),
    )
    field = models.CharField(default = '이수영역 선택', max_length = 10, choices=completion)
    score = models.IntegerField(
        default=5,
        validators=[MaxValueValidator(5), MinValueValidator(1)],
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def short(self):
        return self.body[:25]
        
    def summary(self):
        return self.body[:100]

    class Meta:
        ordering = ['-id']

class Comment(models.Model):
    post = models.ForeignKey(List, on_delete=models.CASCADE, null = True, related_name='comments')
    text = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.text
        
