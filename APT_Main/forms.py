from django import forms
from .models import t001log, t010for, t100lic
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db.models import Max

SETOR_CHOICES = [
    ('TI', 'Tecnologia da Informação'),
    ('RH', 'Recursos Humanos'),
    ('FIN', 'Financeiro'),
    ('ADM', 'Administração'),
    # Adicione outras opções aqui...
]

STATUS_CHOICES = [
    ('A', 'Ativa'),
    ('I', 'Inativa'),
    ('E', 'Expirada')
]

class CredencialForm(forms.ModelForm):
    senha_confirma = forms.CharField(
        widget=forms.PasswordInput(),
        label="Confirme a Senha"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f"{classes} form_cad_credenciais"

    class Meta:
        model = t001log
        fields = ['susrnam', 'susrset', 'susrlog', 'susrsen']
        labels = {
            'susrnam': 'Nome do usuário',
            'susrset': 'Setor',
            'susrlog': 'Email',
            'susrsen': 'Senha',
        }
        widgets = {
            'susrsen': forms.PasswordInput(),
        }

    def clean_susrlog(self):
        email = self.cleaned_data.get('susrlog')
        if t001log.objects.filter(susrlog=email).exists():
            raise ValidationError("Já existe um usuário com este email.")
        return email
    
    def clean_susrnam(self):
        nome = self.cleaned_data.get('susrnam')
        if t001log.objects.filter(susrnam=nome).exists():
            raise ValidationError("Já existe um usuário com este nome")
        return nome

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("susrsen")
        senha_confirma = cleaned_data.get("senha_confirma")

        if senha and senha_confirma and senha != senha_confirma:
            self.add_error('senha_confirma', "As senhas não coincidem.")

        # Criptografa a senha antes de salvar
        if senha:
            cleaned_data["susrsen"] = make_password(senha)

        return cleaned_data
    
class FornecedorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f"{classes} item_form"

    class Meta:
        model = t010for
        fields = ['nforcod', 'sfornam', 'sforcnp']
        labels = {
            'nforcod': 'Código Fornecedor',
            'sfornam': 'Nome Fornecedor',
            'sforcnp': 'CNPJ',
        }

class LicencaForm(forms.ModelForm):

    ssetlic = forms.ChoiceField(choices=SETOR_CHOICES, label='Setor')
    ssetres = forms.ChoiceField(choices=SETOR_CHOICES, label='Setor Responsável')
    ssitlic = forms.ChoiceField(choices=STATUS_CHOICES, label='Status')


    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        self.fields['fdurlic'].widget.attrs['readonly'] = True

        if not self.instance.pk:
            ultimo_codigo = t100lic.objects.aggregate(Max('ncodlic'))['ncodlic__max'] or 0
            self.fields['ncodlic'].initial = ultimo_codigo + 1

        placeholders = {
            'ncodlic': 'Digite o código da licença',
            'snomlic': 'Digite o nome da licença',
            'ssigite': 'Digite a sigla da licença',
            'ssetlic': 'Digite o setor',
            'ddatini': 'DD/MM/AAAA',
            'ddatfin': 'DD/MM/AAAA',
            'fdurlic': 'Duração em dias (Automatico)',
            'ssernum': 'Serial Number',
            'slinsit': 'www.exemplo.com',
            'susrcre': 'Usuário',
            'ssencre': 'Senha',
            'ssetres': 'Setor responsável',
            'sobsadi': 'Observações',
            'ssitlic': 'Ativa/Inativa/etc.',
        }


        for name, field in self.fields.items():
            classes = field.widget.attrs.get('class', '')
            if name in ['ddatini', 'ddatfin']:
                field.widget.attrs['class'] = f"{classes} item_campo_pequeno"
                field.widget.input_type = 'date'
            elif name in ['ncodlic']:
                field.widget.attrs['class'] = f"{classes} item_codigo" 
            else:
                field.widget.attrs['class'] = f"{classes} item_form"

            if name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[name]

    class Meta:
        model = t100lic
        fields = [
            'ncodlic', 'snomlic', 'ssigite', 'ssetlic', 'ddatini', 'ddatfin', 'fdurlic',
            'ssernum', 'slinsit', 'susrcre', 'ssencre', 'ssetres',
            'sobsadi', 'ssitlic'
        ]
        labels = {
            'ncodlic': 'Código da Licença',
            'snomlic': 'Nome da Licença',
            'ssigite': 'Sigla da Licença',
            'ssetlic': 'Setor da Licença',
            'ddatini': 'Data de Início da Licença',
            'ddatfin': 'Data de Fim da Licença',
            'fdurlic': 'Duração (Dias)',
            'ssernum': 'Serial Number da Licença',
            'slinsit': 'Site da Licença',
            'susrcre': 'Credencial de Acesso',
            'ssencre': 'Senha de Acesso',
            'ssetres': 'Setor Responsável pela Renovação',
            'sobsadi': 'Observação Adicional',
            'ssitlic': 'Situação da Licença',
        }
        widgets = {
            'sobsadi': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'item_form'}),
        }
