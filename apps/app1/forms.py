from django import forms


class Login(forms.Form):
    rut = forms.CharField(label='',
                          max_length=12,
                          widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'RUT',
                                                        'id': 'inputUser'})
                          )
    password = forms.CharField(label='',
                               max_length=20,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Contraseña',
                                                                 'id': 'inputPassword'}))

