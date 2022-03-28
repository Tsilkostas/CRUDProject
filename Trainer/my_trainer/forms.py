from django import forms
from . models import Trainer

class TrainerForm(forms.ModelForm):
    
    class Meta:
        model= Trainer
        fields= ('firstname', 'lastname', 'subject')
        
    def __init__(self, *args, **kwargs):
        super(TrainerForm, self).__init__(*args, **kwargs)
        self.fields['subject'].empty_label="Select - subject:"   
    