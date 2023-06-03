from django.db import models
from django import forms
from .models import *

#Группы
class GroupForm(forms.ModelForm):

    @staticmethod
    def clone(request):
        return GroupForm(request)

    @staticmethod
    def clone_instance(ins):
        return GroupForm(instance=ins)

    class Meta:
        model = Groups
        fields = ['group', 'spec', 'num_of_stds']
        widgets = {
                "group": forms.TextInput(attrs={'class': 'input_field'}),
                "spec": forms.TextInput(attrs={'class': 'input_field'}),
                "num_of_stds": forms.NumberInput(attrs={'class': 'input_field'})
        }



#Преподаватели
class PrepodsForm(forms.ModelForm):

    @staticmethod
    def clone(request):
        return PrepodsForm(request)

    @staticmethod
    def clone_instance(ins):
        return PrepodsForm(instance=ins)

    class Meta:
        model = Prepods
        fields = ['fio', 'spec', 'discipline']
        widgets = {
                # "prepod_id": forms.NumberInput(attrs={'class': 'input_field'}),
                "fio": forms.TextInput(attrs={'class': 'input_field'}),
                "spec": forms.TextInput(attrs={'class': 'input_field'}),
                "discipline": forms.TextInput(attrs={'class': 'input_field'})
        }



#Дисциплины
class DisciplinesForm(forms.ModelForm):

    @staticmethod
    def clone(request):
        return DisciplinesForm(request)

    @staticmethod
    def clone_instance(ins):
        return DisciplinesForm(instance=ins)

    class Meta:
        model = Disciplines
        fields = ['name', 'spec', 'prepod']
        widgets = {
            "name": forms.TextInput(attrs={'class': 'input_field'}),
            "spec": forms.TextInput(attrs={'class': 'input_field'}),
            "prepod": forms.TextInput(attrs={'class': 'input_field'}),
        }



#Студенты
class StudentsForm(forms.ModelForm):

    @staticmethod
    def clone(request):
        return StudentsForm(request)

    @staticmethod
    def clone_instance(ins):
        return StudentsForm(instance=ins)

    class Meta:
        model = Students
        fields = ['FIO', 'group']
        widgets = {
            "FIO": forms.TextInput(attrs={'class': 'input_field'}),
            "group": forms.TextInput(attrs={'class': 'input_field'}),
        }


#Справки
class SpravkiForm(forms.ModelForm):

    @staticmethod
    def clone(request):
        return SpravkiForm(request)

    @staticmethod
    def clone_instance(ins):
        return SpravkiForm(instance=ins)

    class Meta:
        model = Spravki
        fields = ['date', 'FIO', 'stip', 'dest']
        widgets = {
            "date": forms.DateTimeInput(attrs={'class': 'input_field'}),
            "FIO": forms.TextInput(attrs={'class': 'input_field'}),
            "stip": forms.NumberInput(attrs={'class': 'input_field'}),
            "dest": forms.TextInput(attrs={'class': 'input_field'}),
        }

