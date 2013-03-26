__author__ = 'michael'

from django import forms

from preferences import preferences

class PollAnswerForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(PollAnswerForm, self).__init__(*args, **kwargs)
        
        self.poll = kwargs['initial'].get('poll')
        
        if self.poll is not None:
            if self.poll.multiple_choice:
                self.fields['answers'] = forms.ModelChoiceField(queryset=self.poll.answers.all())
            else:
                self.fields['answers'] = forms.ModelMultipleChoiceField(queryset=self.poll.answers.all())