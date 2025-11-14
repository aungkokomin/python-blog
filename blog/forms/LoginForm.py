from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="", widget=forms.TextInput(attrs={'id':'id_username' ,'placeholder': 'Username', 'required': 'true'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password','id':'id_password', 'required': 'true'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("Username is required.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("Password is required.")
        return password
