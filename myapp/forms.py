from django import forms
from .models import Resume

GENDER_CHOICES = [
    ('Male' , 'Male'),
    ('Female' , 'Female'),
    ('Others' , 'Others'),
]

JOB_CITY_CHOICE = (
    ('Chittagong','Chittagong'),
    ('Rangpur','Rangpur'),
    ('Rajshahi','Rajshahi'),
    ('Dhaka','Dhaka'),
    ('Jashore','Jashore'),
    ('Dinajpur','Dinajpur'),
    ('Sylhet','Sylhet'),
    ('Pabna ','Pabna '),
    ('Bogra','Bogra'),
    ('Noakhali','Noakhali'),
    ('Faridpur','Faridpur'),
    ('Barisal','Barisal'),
    ('Comilla','Comilla'),
    ('Mymensingh','Mymensingh'),
)

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField( choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Prefered Job Locations',choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        fields = ['name','dob','gender','locality','city','pin',
                'state','mobile','email','job_city','profile','my_file']

        labels = {'name' : 'Full Name','dob' : 'Date Of Birth', 'pin' : 'Pin Code',
                'mobile' : 'Mobile No','email' : 'Email Id','profile' : 'Profile Image',
                'my_file' : 'Document'}
        
        widgets = {
            'name' : forms.TextInput( attrs = { 'class' : 'form-control' } ) ,
            'dob' : forms.DateInput( attrs = { 'class' : 'form-control','id' : 'datepicker' }),
            'locality' : forms.TextInput( attrs = { 'class' : 'form-control' } ),
            'city' : forms.TextInput( attrs = { 'class' : 'form-control' } ),
            'pin' : forms.NumberInput( attrs= {'class' : 'form-control' } ),
            'state' : forms.Select( attrs= { 'class' : 'form-control' } ),
            'mobile' : forms.NumberInput( attrs= { 'class' : 'form-control' } ),
            'email' : forms.EmailInput( attrs= { 'class' : 'form-control' } ),
        }
    
