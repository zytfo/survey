from django import forms

class SurveyForm(forms.Form):
    OPTIONS1 = (('0','Eurasia'),
               ('1','Africa'),
               ('2','North America'),
               ('3','South America'),
               ('4','Australia'),
               ('5','Antarctica'),)
    question1 = forms.MultipleChoiceField(choices=OPTIONS1, widget=forms.CheckboxSelectMultiple())
    OPTIONS2 = (('1','1'),
               ('2','2'),
               ('3','3'),
               ('4','4'),
               ('5','5'),
               ('6','6'),
               ('7','7'),
               ('8','8'),
               ('9','9'),
               ('10','10'),)
    question2 = forms.ChoiceField(choices=OPTIONS2, widget=forms.Select(attrs={'class': 'form-control', 'id': 'selectbasic', 'name': 'selectbasic'}))
    OPTIONS3 = (('1','Yes'),
               ('2','No'),
               ('3',"I'm not sure if it was a PaaS service"),)
    question3 = forms.ChoiceField(required=True, choices=OPTIONS3, widget=forms.RadioSelect(), initial='1')
    OPTIONS4 = (('1','<20'),
               ('2','21-30'),
               ('3','31-40'),
               ('3','41-50'),
               ('3','50+'),)
    question4 = forms.ChoiceField(required=True, choices=OPTIONS4, widget=forms.RadioSelect(attrs={'name': 'radios_age'}), initial='1')
    question5 = forms.CharField(min_length=4, widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'textarea', 'name': 'textarea'}))