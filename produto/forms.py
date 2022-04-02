from django.forms import ModelForm, Select, TextInput, NumberInput, Textarea, FileInput

from produto.models import Produto, Categoria, Marca


class FormProduto(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nome do produto'
            }),
            'descricao': Textarea(attrs={
                'class': "form-control mt-3 mb-3",
                'placeholder': 'Insira a descrição do produto...',
                'style': 'resize: None;'
            }),
            'quantidade': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Quantidade',
                'step': 1
            }),
            'imagem': FileInput(attrs={
                'class': "form-control me-2",
                'style': 'max-width: 300px;'
            }),
            'preco': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'R$',
                'step': 0.01,
                'min': 0
            }),
            'preco_promocional': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'R$',
                'step': 0.01,
                'min': 0
            }),
            'categoria': Select(attrs={
                'class': "form-select",
            }),
            'Especificacoes': Select(attrs={
                'class': "form-select",
            }),
            'marca': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Marca do produto',
            }),

        }

class FormCategoriaProduto(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nome da categoria',
            }),
        }
class FormMarcaProduto(ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nome da marca',
            }),
        }


