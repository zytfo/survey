from django import forms
from django.contrib.auth import authenticate
from .localizations import Localization as locale

class SurveyForm(forms.Form):
    #question1 = forms.MultipleChoiceField(choices=locale.survey_form['en']['question_1_choices'], widget=forms.CheckboxSelectMultiple())
    question2 = forms.ChoiceField(choices=locale.survey_form['all']['question_2_choices'], widget=forms.Select(attrs={'class': 'form-control', 'id': 'selectbasic', 'name': 'selectbasic'}))
    question3 = forms.ChoiceField(required=True, choices=locale.survey_form['en']['question_3_choices'], widget=forms.RadioSelect(), initial='0')
    question4 = forms.ChoiceField(required=True, choices=locale.survey_form['all']['question_4_choices'], widget=forms.RadioSelect(attrs={'name': 'radios_age'}), initial='0')
    question5 = forms.CharField(min_length=256, widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'textarea', 'name': 'textarea'}))
    question6 = forms.MultipleChoiceField(choices=locale.survey_form['all']['question_6_choices'], widget=forms.CheckboxSelectMultiple())

class SurveyFormRu(forms.Form):
    #question1 = forms.MultipleChoiceField(choices=locale.survey_form['ru']['question_1_choices'], widget=forms.CheckboxSelectMultiple())
    question2 = forms.ChoiceField(choices=locale.survey_form['all']['question_2_choices'], widget=forms.Select(attrs={'class': 'form-control', 'id': 'selectbasic', 'name': 'selectbasic'}))
    question3 = forms.ChoiceField(required=True, choices=locale.survey_form['ru']['question_3_choices'], widget=forms.RadioSelect(), initial='0')
    question4 = forms.ChoiceField(required=True, choices=locale.survey_form['all']['question_4_choices'], widget=forms.RadioSelect(attrs={'name': 'radios_age'}), initial='0')
    question5 = forms.CharField(min_length=256, widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'textarea', 'name': 'textarea'}))
    question6 = forms.MultipleChoiceField(choices=locale.survey_form['all']['question_6_choices'], widget=forms.CheckboxSelectMultiple())

class LoginForm(forms.Form):
  username = forms.CharField(max_length=255, required=True)
  password = forms.CharField(widget=forms.PasswordInput, required=True)

  def clean(self):
      username = self.cleaned_data.get('username')
      password = self.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if not user or not user.is_active:
          raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
      return self.cleaned_data

  def login(self, request):
      username = self.cleaned_data.get('username')
      password = self.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      return user