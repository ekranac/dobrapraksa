from django.forms import ModelForm
from example.models import Comment


class CreateCommentForm(ModelForm):
    class Meta:
        model=Comment
        fields= ["content"]
