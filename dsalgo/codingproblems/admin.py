from django.contrib import admin
from codingproblems.models import Category, CodingProblem, Solution, Language, Author

# Register your models here.
admin.site.register(Category)
admin.site.register(CodingProblem)
admin.site.register(Solution)
admin.site.register(Language)
admin.site.register(Author)