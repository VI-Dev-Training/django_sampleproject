from django.forms import ModelForm, fields
from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'project_image',
            'description',
            'demo_link',
            'tags'
        ]


class addReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']