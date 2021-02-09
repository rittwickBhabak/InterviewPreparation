from django.shortcuts import render, redirect 
from django.contrib import messages
from codingproblems.models import CodingProblem, Author, Solution 

def index(request):
    section1 = Author.objects.filter(auth='Section1')[0]
    section2 = Author.objects.filter(auth='Section2')[0]
    miscellaneous = Author.objects.filter(auth='Miscellaneous')[0]

    solved_section1 = len(CodingProblem.objects.filter(status=True, auth=section1))
    solved_section2 = len(CodingProblem.objects.filter(status=True, auth=section2))
    solved_miscellaneous = len(CodingProblem.objects.filter(status=True, auth=miscellaneous))

    total_section1 = len(CodingProblem.objects.filter(auth=section1))
    total_section2 = len(CodingProblem.objects.filter(auth=section2))
    total_miscellaneous = len(CodingProblem.objects.filter(auth=miscellaneous))
    def percent(solved, total):
        if total==0:
            return 0
        else:
            return int(solved/total*100)
    context = {
        'solved_section1': solved_section1,
        'solved_section2': solved_section2,
        'solved_miscellaneous': solved_miscellaneous,
        'total_section1': total_section1,
        'total_section2': total_section2,
        'total_miscellaneous': total_miscellaneous,
        'percent_section1': percent(solved_section1, total_section1),
        'percent_section2': percent(solved_section2, total_section2),
        'percent_miscellaneous': percent(solved_miscellaneous, total_miscellaneous)
    }
    return render(request, 'index.html', context)

def search(request):
    query = request.GET.get('q').split(' ')


    search_list_codingproblems = CodingProblem.objects.filter(pk='-1')
    search_list_solutions = Solution.objects.filter(pk=-1)
    for q in query:
        search_list_codingproblems = search_list_codingproblems | CodingProblem.objects.filter(problem_statement__icontains=q)
        search_list_solutions = search_list_solutions | Solution.objects.filter(title__icontains=q)
        search_list_solutions = search_list_solutions | Solution.objects.filter(title__icontains=q)


    context = {
        'search_list_codingproblems': search_list_codingproblems,
        'search_list_solutions': search_list_solutions
    }
    return render(request, 'search.html', context)


