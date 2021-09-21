from django import forms
from .models import DesignerRegister, ProjectDescriptionModel, ProjectTagsModel
from .models import DesignerExperience, DesignerEducation



class DesignerRegisterForm(forms.ModelForm):
    class Meta:
        model = DesignerRegister
        fields = [ 'full_name', 'location', 'designer_type','bio', 'top_skills', 'your_photo','experience', 'tools_of_choice', 'cover_photo', 'current_status', 'years_of_experience', 'resume', 'portfolio_link', 'facebook_link', 'twitter_link', 'linkedin_link', 'instagram_link' ]
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder':'Enter Your full name seperated by space'}),
            'location': forms.TextInput(attrs={"placeholder": 'Enter your current location'}),
            'bio': forms.TextInput(attrs={'placeholder':'Write something about yourself'}),
            'experience': forms.TextInput(attrs={'placeholder': 'Your Experience e.g B2B Products, Design System'}),
            'tools_of_choice': forms.TextInput(attrs={'placeholder':'Tools you prefer. E.g. Figma , Invision'}),
            'current_status': forms.TextInput(attrs={'placeholder': 'Your current role. E.g. UX Designer at UBER'}),
            'years_of_experience': forms.NumberInput(attrs={'placeholder': 'Years you have worked in this field.'}),
            'your_photo': forms.FileInput(attrs={'class':'form-control', 'id':'customFile'}),
            'cover_photo': forms.FileInput(attrs={'class':'form-control', 'id':'customFile'}),
            'resume': forms.FileInput(attrs={'class':'form-control', 'id':'customFile'}),
            'top_skills': forms.TextInput(attrs={"placeholder":'Enter your top skills E.g. Whiteboarding, Wireframing'}),
            'portfolio_link': forms.TextInput(attrs={"placeholder":"Enter your porfolio link"}),
            'facebook_link': forms.TextInput(attrs={"placeholder":"Enter your facebook link"}),
            'twitter_link': forms.TextInput(attrs={"placeholder":"Enter your twitter link"}),
            'linkedin_link': forms.TextInput(attrs={"placeholder":"Enter your linkedin link"}),
            'instagram_link': forms.TextInput(attrs={"placeholder":"Enter your instagram link"}),

        }
        


class ProjectDescriptionForm(forms.ModelForm):
    class Meta:
        model = ProjectDescriptionModel
        fields = ['project_name','project_link','project_description','problem', 'scope', 'audience', 'ideation', 'competitors', 'challenges']

class ProjectTagsForm(forms.ModelForm):
    class Meta:
        model = ProjectTagsModel
        fields = ['project_type', 'platform_used', 'project_stage', 'people_collab_with']

class DesignerExperienceForm(forms.ModelForm):
    class Meta:
        model = DesignerExperience
        fields = [ 'date_from', 'date_to', 'work_title', 'work_location', 'work_description', 'skills', 'tools_used' ]
        widgets = {
            'date_from': forms.DateInput(attrs={'type':'date'}),
            'date_to': forms.DateInput(attrs={'type':'date'}),
            'work_title': forms.TextInput(attrs={'placeholder':'Position and Company. E.g. Senior UX Designer at UBER'}),
            'work_location': forms.TextInput(attrs={'placeholder':"Location of your Company"}),
            'work_description': forms.Textarea(attrs={"placholder":"What you did at that company"}),
            'skills': forms.TextInput(attrs={"placeholder":"Skills you learned. E.g. Whiteboarding, wireframing"}),
            'tools_used': forms.TextInput(attrs={'placeholder':"Tools you used. E.g. Figma, MIRO, Invision, Airtable"})
            }
        

class DesignerEducationForm(forms.ModelForm):
    class Meta:
        model = DesignerEducation
        fields = [ 'date_from', 'date_to', 'education_title', 'location_of_instution', 'description', 'grade']
        widgets = {
            'date_from': forms.DateInput(attrs={'type':'date'}),
            'date_to': forms.DateInput(attrs={'type':'date'}),
            'education_title': forms.TextInput(attrs={'placeholder':'E.g. High School, College'}),
            'location_of_instution': forms.TextInput(attrs={'placholder':"Place where your instutite was located."}),
            'description': forms.TextInput(attrs={"placeholder":"Tell us about what you did, what you learned."}),
            'grade': forms.TextInput(attrs={"placholder":"E.g. A, B, C"}),
            }