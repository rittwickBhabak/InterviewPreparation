from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect 
from codingproblems.models import Category, CodingProblem, Solution, Author
from django.contrib import messages
from codingproblems.forms import CodingProblemForm, SolutionForm

# Create your views here.
def section1(request):
    try:
        categories = Category.objects.all()
        auth = Author.objects.filter(auth='Section1')[0]
        problems_list = []
        for category in categories:
            coding_problems = CodingProblem.objects.filter(cat=category, auth=auth)
            solved_coding_problems = CodingProblem.objects.filter(cat=category, auth=auth, status=True)
            if len(coding_problems)>0:
                problems_list.append({'category': category, 
                                    'problems':coding_problems,
                                    'no_of_solved_problems': len(solved_coding_problems)})
        context = {
            'problems_list' : problems_list,
            'heading':'Section1'
        }
        return render(request, 'codingproblems/index.html', context)
    except Exception as e:
        print(e)
        messages.warning(request, 'Some error occoured')
        return redirect('/')

def section2(request):
    try:
        categories = Category.objects.all()
        auth = Author.objects.filter(auth='Section2')[0]
        problems_list = []
        for category in categories:
            coding_problems = CodingProblem.objects.filter(cat=category, auth=auth)
            solved_coding_problems = CodingProblem.objects.filter(cat=category, auth=auth, status=True)
            if len(coding_problems)>0:
                problems_list.append({'category': category, 
                                    'problems':coding_problems,
                                    'no_of_solved_problems': len(solved_coding_problems)})
        context = {
            'problems_list' : problems_list,
            'heading':'Section2'
        }
        return render(request, 'codingproblems/index.html', context)
    except:
        messages.warning(request, 'Some error occoured')
        return redirect('/')


def miscellaneous(request):
    try:
        categories = Category.objects.all()
        auth = Author.objects.filter(auth='Miscellaneous')[0]
        problems_list = []
        for category in categories:
            coding_problems = CodingProblem.objects.filter(cat=category, auth=auth)
            solved_coding_problems = CodingProblem.objects.filter(cat=category, auth=auth, status=True)
            if len(coding_problems)>0:
                problems_list.append({'category': category, 
                                    'problems':coding_problems,
                                    'no_of_solved_problems': len(solved_coding_problems)})
        context = {
            'problems_list' : problems_list,
            'heading':'Miscellaneous'
        }
        return render(request, 'codingproblems/index.html', context)
    except:
        messages.warning(request, 'Some error occoured')
        return redirect('/')



def newproblem(request):
    try:
        form = CodingProblemForm()

        if request.method == 'POST':
            form = CodingProblemForm(request.POST)

            if form.is_valid():
                form.save(commit=True)
                messages.success(request, "Coding Problem added successfully")
                return redirect('/')
        return render(request, 'codingproblems/newproblem.html', { 'form':form })
    except:
        messages.warning(request, 'Some error occoured')
        return redirect('/')


def newsolution(request, pk):
    try:
        form = SolutionForm()
        problem = CodingProblem.objects.get(pk=pk)
        if request.method == 'POST':
            form = SolutionForm(request.POST)

            if form.is_valid():
                form.save(commit=True)
                problem.status = True 
                problem.save()
                path = '/'.join(['', 'codingproblems','problem',str(problem.pk)])
                return redirect(path)
        return render(request, 'codingproblems/newsolution.html', { 'form':form, 'pk':problem.pk })
    except:
        messages.warning(request, 'Some error occoured')
        return redirect('/')

def deletenewsolution(request, pk):
    if request.method =='POST':
        solution = Solution.objects.get(pk=pk)
        if solution:
            problem = CodingProblem.objects.get(pk=solution.problem_id.pk)
            solutions = Solution.objects.filter(problem_id=problem)
            if len(solutions)==1:
                problem.status = False
                problem.save()
            solution.delete()
            messages.success(request, 'Solution deletion successful')
            path = '/'.join(['', 'codingproblems', 'problem', str(problem.pk)])
            return redirect(path)
        messages(request, 'Solution not found')
        return redirect('/')
    return redirect('/')

def updatenewsolution(request, pk):
    try:
        form = SolutionForm()
        solution = Solution.objects.get(pk=pk)
        form = SolutionForm(request.POST or None, instance=solution)
        if request.method == 'POST':
            form = SolutionForm(request.POST, instance=solution)

            if form.is_valid():
                form.save(commit=True)
                path = '/'.join(['', 'codingproblems','solution',str(solution.pk)])
                messages.success(request, 'Soluiton updated successful')
                return redirect(path)
        return render(request, 'codingproblems/updatesolution.html', { 'form':form, })
    except:
        messages.warning(request, 'Some error occoured')
        return redirect('/')

def problem(request, pk):
    try:
        problem = CodingProblem.objects.get(pk=pk)
        if problem:
            solutions = Solution.objects.filter(problem_id=problem)
            return render(request, 'codingproblems/problem.html', { 'problem': problem, 'solutions': solutions })
        else:
            messages.warning(request, 'Coding Problem not found')
            return redirect('/')
    except:
        messages.warning(request, 'Some error occoured')
        return redirect('/')

def solution(request, pk):
    try:
        solution = Solution.objects.get(pk=pk)
        if solution:
            print(solution.problem_id.problem_statement)
            return render(request, 'codingproblems/solution.html', {'solution':solution})
        else:
            messages.warning(request, 'Solution not found')
            return redirect('/')
    except:
        messages.warning(request, 'Some error occoured')
        return redirect('/')