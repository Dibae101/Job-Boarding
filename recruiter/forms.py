from django import forms
from .models import RecruiterRegister


# industry = (
#     ('accounting', 'Accounting'),
#     ('animation', 'Animation'),
#     ('apparel and fashion', 'Apparel and Fashion'),
#     ('arts and crafts', 'Arts and Crafts'),
#     ('aanking', 'Banking'),
#     ('computer games', 'Computer Games'),
#     ('computer networking', 'Computer Networking'),
#     ('cosmetics', 'Cosmetics'),
#     ('fine arts', 'Fine Arts'),
#     ('financial services', 'Financial Services'),
#     ('food and beverages', 'Food and Beverages'),   
#     )
# size = (
#     ('1-10', '1-10'),
#     ('11-50', '11-50'),
#     ('51-100', '51-100'),
#     ('101-250', '101-250'),
#     ('251-1000', '251-1000'),
#     ('1001-2500', '1001-2500'),
#     ('2501+', '2501+'),
#     )

class RecruiterRegisterForm(forms.ModelForm):
    class Meta:
        model = RecruiterRegister
        fields = ['id', 'image', 'name', 'location', 'industry', 'size', 'company_name']
        
        labels = { 'image': "Porfile Picture*", 'name': 'Name*',  'location': 'Location*',
            'industry': 'What industry are you in?*', 'size': 'What is the size of your company?*', 
            'company_name': 'Company Name*'
        }
        
        widgets = { 'name': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                'location': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                'company_name': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),}
        
