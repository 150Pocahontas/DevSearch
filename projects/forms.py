from django.forms import ModelForm, widgets
from django import forms
from .models import Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'feature_image', 'description', 'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwagrs):
        super(ProjectForm, self).__init__(*args,**kwagrs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
    
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        lables = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote' 
        }

    def __init__(self, *args, **kwagrs):
        super(ReviewForm, self).__init__(*args,**kwagrs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
