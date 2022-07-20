from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from .models import Campana, Multimedia

class CreateFormCampana(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']="form-control"
    class Meta:
        model = Campana
        fields='__all__'
        exclude = ('empresa',)

class UpdateFormCampana(CreateFormCampana):
    pass
        

class CreateFormMultimedia(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']="form-control"
    class Meta:
        model = Multimedia
        fields='__all__'
        exclude = ('capana',)


class UpdateFormMultimedia(CreateFormMultimedia):
    pass



