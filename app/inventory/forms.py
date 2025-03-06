from django import forms
from .models import Computer, Printer, Accessory


class MyComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_type', 'computer_inventory', 'computer_snumber', 'computer_location']
        widgets = {
            'computer_type': forms.Select(attrs={'class': 'form-control'}),
            'computer_inventory': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите инвентарный номер'}),
            'computer_snumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите серийный номер'}),
            'computer_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите расположение'}),
        }


class MyPrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = ['printer_type', 'printer_inventory', 'printer_snumber', 'printer_location']
        widgets = {
            'printer_type': forms.Select(attrs={'class': 'form-control'}),
            'printer_inventory': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите инвентарный номер'}),
            'printer_snumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите серийный номер'}),
            'printer_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите расположение'}),
        }

class MyAccessoryForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = ['accessory_type', 'accessory_inventory', 'accessory_snumber', 'accessory_location']
        widgets = {
            'accessory_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите наименование устройства'}),
            'accessory_inventory': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите инвентарный номер'}),
            'accessory_snumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите серийный номер'}),
            'accessory_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите расположение'}),
        }

