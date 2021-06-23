from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Senha',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita a senha',
                                widget=forms.PasswordInput)
    username = forms.CharField(label='Login', widget=forms.TextInput(
        attrs={'class': 'formcontrol', 'required': 'true'}))
    first_name = forms.CharField(label='Primeiro Nome', widget=forms.TextInput(
        attrs={'class': 'formcontrol', 'required': 'false'}))
    email = forms.CharField(label='E-mail', widget=forms.TextInput(
        attrs={'class': 'formcontrol', 'required': 'true'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(label='Primeiro Nome', widget=forms.TextInput(
        attrs={'class':'formcontrol', 'required': 'true'}))
    last_name = forms.CharField(label='Segundo Nome', widget=forms.TextInput(
        attrs={'class':'formcontrol', 'required': 'false'}))
    email = forms.CharField(label='Endereço de E-mail', widget=forms.TextInput(
        attrs={'class':'formcontrol', 'required': 'true'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    datanascimento = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"), required=False, label='Data de Nascimento')
    endereco = forms.CharField(label='Endereço Completo', required=False, widget=forms.TextInput(
        attrs={'class':'formcontrol'}))
    telefone = forms.CharField(label='Telefone', required=False, widget=forms.TextInput(
        attrs={'class': 'formcontrol'}))
    estadocivil = forms.SelectMultiple(
        attrs={'class': 'formcontrol', 'required': 'false'})
    necessidade = forms.BooleanField(label='Possui alguma necessidade especial?', required=False)
    necessidadecategoria = forms.CharField(label='Especifique a necessidade especial', required=False, widget=forms.TextInput(
        attrs={'class': 'formcontrol'}))
    carteira = forms.BooleanField(label='Possui carteira de motorista?', required=False)
    carteiracategoria = forms.SelectMultiple(
        attrs={'class': 'formcontrol', 'required': 'false'})
    areainteresse = forms.SelectMultiple(
        attrs={'class': 'formcontrol', 'required': 'false'})
    escolaridade = forms.SelectMultiple(
        attrs={'class': 'formcontrol', 'required': 'false'})
    instituicao = forms.CharField(label='Instituições e Cursos',required=False, widget=forms.Textarea(
        attrs={'class': 'formcontrol', 'rows':'5'}))
    empresa1 = forms.CharField(label='Empresa 1', required=False, widget=forms.TextInput(
        attrs={'class':'formcontrol'}))
    datainicio1 = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"), required=False,
                                     label='Data Início')
    datasaida1 = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"), required=False,
                                     label='Data Saída')
    cargo1 = forms.CharField(label='Cargo', required=False, widget=forms.TextInput(
        attrs={'class':'formcontrol'}))
    atividades1 = forms.CharField(label='Descreva as principais atividade da Empresa 1',required=False, widget=forms.Textarea(
        attrs={'class': 'formcontrol', 'rows':'3'}))
    empresa2 = forms.CharField(label='Empresa 2', required=False, widget=forms.TextInput(
        attrs={'class':'formcontrol'}))
    datainicio2 = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"), required=False,
                                     label='Data Início')
    datasaida2 = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"), required=False,
                                     label='Data Saída')
    cargo2 = forms.CharField(label='Cargo', required=False, widget=forms.TextInput(
        attrs={'class':'formcontrol'}))
    atividades2 = forms.CharField(label='Descreva as principais atividade da Empresa 2',required=False, widget=forms.Textarea(
        attrs={'class': 'formcontrol', 'rows':'3'}))
    empresa3 = forms.CharField(label='Empresa 3', required=False, widget=forms.TextInput(
        attrs={'class':'formcontrol'}))
    datainicio3 = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"), required=False,
                                     label='Data Início')
    datasaida3 = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"), required=False,
                                     label='Data Saída')
    cargo3 = forms.CharField(label='Cargo', required=False, widget=forms.TextInput(
        attrs={'class':'formcontrol'}))
    atividades3 = forms.CharField(label='Descreva as principais atividade da Empresa 3',required=False, widget=forms.Textarea(
        attrs={'class': 'formcontrol', 'rows':'3'}))
    linkedin = forms.CharField(label='Endereço Linkedin', required=False, widget=forms.TextInput(
        attrs={'class':'formcontrol'}))
    aceitetermo = forms.BooleanField(error_messages={'required': 'Este campo é obrigatório!'}, label='Estou de acordo com os termos.')


    class Meta:
        model = Profile
        fields = ('datanascimento','endereco', 'telefone', 'estadocivil', 'necessidade', 'necessidadecategoria', 'carteira', 'carteiracategoria',
                  'areainteresse', 'escolaridade', 'instituicao', 'empresa1', 'empresa2', 'empresa3', 'datainicio1',
                  'datainicio2', 'datainicio3','datasaida1', 'datasaida2', 'datasaida3', 'cargo1', 'cargo2', 'cargo3',
                  'atividades1', 'atividades2', 'atividades3', 'linkedin', 'aceitetermo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['datanascimento'].widget.attrs.update({'class': 'mask-data'})
        self.fields['datainicio1'].widget.attrs.update({'class': 'mask-data'})
        self.fields['datainicio2'].widget.attrs.update({'class': 'mask-data'})
        self.fields['datainicio3'].widget.attrs.update({'class': 'mask-data'})
        self.fields['datasaida1'].widget.attrs.update({'class': 'mask-data'})
        self.fields['datasaida2'].widget.attrs.update({'class': 'mask-data'})
        self.fields['datasaida3'].widget.attrs.update({'class': 'mask-data'})
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})

class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')