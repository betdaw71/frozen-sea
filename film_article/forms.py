from django import forms

class ComentForm(forms.Form):
	comment = forms.CharField(label = u'Enter Comment here:',widget=forms.TextInput(attrs={'size': '25em'}))