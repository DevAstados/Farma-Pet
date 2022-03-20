from django.forms import ModelForm, Select, TextInput, NumberInput

from funcionario.models import Funcionario


class FormFuncionario(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'
        widgets = {
            'id': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'ID',
            }),
            'nome': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nome do produto'
            }),
            'usuario': Select(attrs={
                'class': "form-select",
                'placeholder': 'Selecione o usuário'
            }),
        }
