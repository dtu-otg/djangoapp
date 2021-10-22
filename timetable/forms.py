# from django import forms
# from django.utils.safestring import mark_safe
from django.forms import ModelForm, inlineformset_factory
from .models import Slot, Course

# class TTForm(forms.Form):
#     course_code = forms.CharField(label=mark_safe("Course Code"), max_length=10)
#     course_name = forms.CharField(label=mark_safe("Course Name"), max_length=100)

class SlotForm(ModelForm):
    class Meta:
        model = Slot
        fields = ['day', 'time', 'course']

class TTForm(ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name', 'islab', 'group', 'batch', 'prof_name', 'prof_mail']
        labels = {'code': 'Course Code', 'name': 'Course Name', 'islab': 'Is it LAB?', 'prof_name': 'Faculty Name', 'prof_mail': 'Faculty Email'}


TTFormSet = inlineformset_factory(Course, Slot, SlotForm, extra=5)