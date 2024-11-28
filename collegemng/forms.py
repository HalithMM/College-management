from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . models import Teacher,Student

class TeacherSignup(UserCreationForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Firstname',
        'class'      :'form-control',
    }))
    lastname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Lastname',
        'class'      :'form-control',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'E-mail',
        'class'      :'form-control',
    }))
    register_id = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Register Id',
        'class'      :'form-control',
    }))
    class Meta :
        model = Teacher
        fields = ['firstname','lastname','email','register_id','password1', 'password2']

class TeacherLogin(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Email',
        'class':'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput (attrs={
        'placeholder':'Enter password',
        'class'      : 'form-control ',
    }))

class StudentDetails(forms.ModelForm):
    Profile_pic = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'class': 'form-control',
        'accept': 'image/*',  
    }), required=True)

    firstname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Firstname',
        'class': 'form-control',
    }))
    lastname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Lastname',
        'class': 'form-control',
    }))
    register_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Register Id',
        'class': 'form-control',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'E-mail',
        'class': 'form-control',
    }))
    DoB = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))
    Gender = forms.ChoiceField(
        choices=Student.GENDER_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    Blood_group = forms.ChoiceField(
        choices=Student.BLOOD_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    Address = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Address',
        'class': 'form-control',
        'rows': 3,
    }))
    City = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'City',
        'class': 'form-control',
    }))
    State = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'State',
        'class': 'form-control',
    }))

    class Meta:
        model = Student
        fields = [
            'Profile_pic', 'firstname', 'lastname', 'register_number', 'email', 
            'DoB', 'Gender', 'Blood_group', 'Address', 'City', 'State'
        ]
