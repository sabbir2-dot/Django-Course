from django import forms
from django.core import validators
# widget will convert field to html input 

class contactForm(forms.Form):
    name = forms.CharField(label="User Name", initial="Sabbir", help_text="Enter Your Full Name", widget=forms.Textarea(attrs = {'id' : 'text_area', 'placeholder': "Enter your name"}))
    # file = forms.FileField()
    email = forms.EmailField(label="User Email")
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthDate = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    Choices = [('S','Small'), ('M',"Medium"), ('L', 'Large')]
    size = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)
    MEAL = [('P', 'Pepparoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     return valname
    
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com")
    #     return valemail

# to validate all data we use a shortcut

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com")

# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput, validators=[validators.MaxLengthValidator(limit_value=8,message="Your Name Can Have Maximum 8 Characters"), validators.MinLengthValidator(limit_value=3, message="Your Name Must Have Minimum 3 Characters")])
#     email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a Valid Email")])
#     age = forms.IntegerField()
#     file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'])])

class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data =  super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 5:
            raise forms.ValidationError("Name must be at least 5 characters long")

