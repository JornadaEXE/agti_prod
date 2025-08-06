from django import forms
from .models import t001log, t010for, t100lic, t011lan, t200ipc, t002set, t003tip, t004eqp
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db.models import Max
from django.contrib.auth.models import User

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
        #    'ncodlic': 'Digite o código da licença',
        #    'snomlic': 'Digite o nome da licença',
        #    'ssigite': 'Digite a sigla da licença',
        #    'ssetlic': 'Digite o setor',
        #    'ddatini': 'DD/MM/AAAA',
        #    'ddatfin': 'DD/MM/AAAA',
        #    'fdurlic': 'Duração em dias (Automatico)',
        #    'ssernum': 'Serial Number',
            'slinsit': 'www.exemplo.com',
        #    'susrcre': 'Usuário',
        #    'ssencre': 'Senha',
        #    'ssetres': 'Setor responsável',
        #    'sobsadi': 'Observações',
        #    'ssitlic': 'Ativa/Inativa/etc.',
        }


        for name, field in self.fields.items():
            classes = field.widget.attrs.get('class', '')
            if name in ['ncodlic', 'snomlic', 'ssitlic']:
                    field.widget.attrs['class'] = f"{classes} item_codigo"
            else:
                if name in ['ddatini', 'ddatfin']:
                    field.widget.attrs['class'] = f"{classes} item_campo_pequeno"
                    field.widget.input_type = 'date'
                elif name in ['sobsadi']:
                    field.widget.attrs['class'] = f"{classes} csf5" 
                else:
                    field.widget.attrs['class'] = f"{classes} fcp1"

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
            'ncodlic': 'Código',
            'snomlic': 'Nome',
            'ssigite': 'Sigla',
            'ssetlic': 'Setor',
            'ddatini': 'Data Inicial',
            'ddatfin': 'Data Final',
            'fdurlic': 'Duração',
            'ssernum': 'Serial Number',
            'slinsit': 'Site',
            'susrcre': 'Usuário',
            'ssencre': 'Senha',
            'ssetres': 'Setor Responsável',
            'sobsadi': 'Observação',
            'ssitlic': 'Status',
        }
        widgets = {
            'sobsadi': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'item_form'}),
        }

class LancamentoForm(forms.ModelForm):

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
    
        for name, field in self.fields.items():
            classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f"{classes} item_codigo"

    class Meta:
        model = t011lan
        fields = ['nfilcod', 'ncnpfor', 'snomfor', 'ddatemi', 'ddatven', 'nvlrlan',
                  'ncodsol', 'ncodcon', 'ncodtra', 'scodccu', 'sobslan']

class CadastroUserForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    senha_confirma = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f"{classes} itc1"

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        senha_confirma = cleaned_data.get('senha_confirma')

        if senha and senha_confirma and senha != senha_confirma:
            raise ValidationError('As senhas não coincidem.')
        
        return cleaned_data
    
class EndEqpForm(forms.ModelForm):

    stipeqp = forms.ModelChoiceField(
        queryset=t003tip.objects.all(),
        empty_label="Selecione um Tipo",
        to_field_name="scodtip"
    )

    snomset = forms.ModelChoiceField(
        queryset=t002set.objects.all(),
        empty_label="Selecione um Setor",
        to_field_name="ssetnam"
    )

    smodeqp = forms.ModelChoiceField(
        queryset=t004eqp.objects.all(),
        empty_label="Selecione um Equipamento",
        to_field_name="seqpnam"
    )



    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
    
        for name, field in self.fields.items():
            classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f"{classes} cforend1"

            help_text = self._meta.model._meta.get_field(name).help_text
            if help_text:
                field.label = help_text

    class Meta:
        model = t200ipc
        fields = '__all__'

class CadTipForm(forms.ModelForm):

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
    
        for name, field in self.fields.items():
            classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f"{classes} cforend1"

            help_text = self._meta.model._meta.get_field(name).help_text
            if help_text:
                field.label = help_text

    class Meta:
        model = t003tip
        fields = '__all__'

class CadEqpForm(forms.ModelForm):

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
    
        for name, field in self.fields.items():
            classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f"{classes} cforend1"

            help_text = self._meta.model._meta.get_field(name).help_text
            if help_text:
                field.label = help_text

    class Meta:
        model = t004eqp
        fields = '__all__'

class CadSetForm(forms.ModelForm):

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
    
        for name, field in self.fields.items():
            classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f"{classes} cforend1"

            help_text = self._meta.model._meta.get_field(name).help_text
            if help_text:
                field.label = help_text

    class Meta:
        model = t002set
        fields = '__all__'


