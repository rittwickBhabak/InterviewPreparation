from django import forms 
from codingproblems.models import CodingProblem, Solution

class CodingProblemForm(forms.ModelForm):
    class Meta:
        model = CodingProblem
        fields = "__all__"
    
class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = "__all__"