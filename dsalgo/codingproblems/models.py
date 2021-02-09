from django.db import models
from ckeditor.fields import RichTextField 
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    cat = models.CharField(max_length=128)
    def __str__(self):
        return f"{self.cat}" 

class Language(models.Model):
    lan = models.CharField(max_length=128)
    def __str__(self):
        return f"{self.lan}"

class Author(models.Model):
    auth = models.CharField(max_length=128)
    def __str__(self):
        return f"{self.auth}"

class CodingProblem(models.Model):
    problem_statement = models.CharField(max_length=128)
    status = models.BooleanField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    auth = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.problem_statement} | {self.cat}" 

class Solution(models.Model):
    problem_id = models.ForeignKey(CodingProblem, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    description = RichTextUploadingField()
    code = models.TextField(default='')
    title = models.CharField(max_length=128, default='Solution')

    def __str__(self):
        return f"Problem: {self.problem_id.problem_statement} | Solution in {self.language}: {self.title}"


