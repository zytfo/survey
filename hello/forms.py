from django import forms

class SurveyForm(forms.Form):
    OPTIONS1 = (('0','Simulator'),
               ('1','Adventure'),
               ('2','Open world'),
               ('3','Platform'),
               ('4','Sports'),
               ('5','Racing'),
               ('6','Strategy'),
               ('7','Shooter'),)
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

    OPTIONS3 = (('0','Yes'),
               ('1','No'),
               ('2',"I'm not sure"),)
    question3 = forms.ChoiceField(required=True, choices=OPTIONS3, widget=forms.RadioSelect(), initial='0')

    OPTIONS4 = (('0','<20'),
               ('1','21-30'),
               ('2','31-40'),
               ('3','41-50'),
               ('4','50+'),)
    question4 = forms.ChoiceField(required=True, choices=OPTIONS4, widget=forms.RadioSelect(attrs={'name': 'radios_age'}), initial='0')

    question5 = forms.CharField(min_length=4, widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'textarea', 'name': 'textarea'}))

class SurveyFormRu(forms.Form):
    OPTIONS1 = (('0','Симуляторы'),
               ('1','Приключенческие'),
               ('2','Открытый мир'),
               ('3','Платформеры'),
               ('4','Спортивные'),
               ('5','Гонки'),
               ('6','Стратегии'),
               ('7','Шутеры'),)
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

    OPTIONS3 = (('0','Да'),
               ('1','Нет'),
               ('2',"Я не уверен"),)
    question3 = forms.ChoiceField(required=True, choices=OPTIONS3, widget=forms.RadioSelect(), initial='0')

    OPTIONS4 = (('0','<20'),
               ('1','21-30'),
               ('2','31-40'),
               ('3','41-50'),
               ('4','50+'),)
    question4 = forms.ChoiceField(required=True, choices=OPTIONS4, widget=forms.RadioSelect(attrs={'name': 'radios_age'}), initial='0')

    question5 = forms.CharField(min_length=4, widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'textarea', 'name': 'textarea'}))
