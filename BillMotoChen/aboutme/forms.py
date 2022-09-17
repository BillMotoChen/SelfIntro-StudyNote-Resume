from django import forms

class PieceSearchForm(forms.Form):
    composer = forms.CharField(label='composer')
    tonality = forms.IntegerField()
    status = forms.IntegerField()