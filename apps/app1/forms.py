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


class CambioPassword(forms.Form):
    previous = forms.CharField(label = 'Contraseña anterior ', widget=forms.PasswordInput(render_value=True))
    new = forms.CharField(label = 'Nueva contraseña ', widget=forms.PasswordInput(render_value=True))
    confirmation = forms.CharField(label = 'Confirme su nueva contraseña ', widget=forms.PasswordInput(render_value=True))