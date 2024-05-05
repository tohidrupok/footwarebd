# from django import forms
# from .models import Resume

# class ResumeForm(forms.ModelForm):
#     class Meta:
#         model = Resume
#         fields = ['resume']


from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['resume', 'name', 'experience', 'position', 'contact', 'email', 'expected_salary', 'remark']
