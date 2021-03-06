from django import forms

from .models import Participant, PageRating


class ParticipantCreateForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['gender', 'age', 'education', 'student']
        widgets = {
            'gender': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'age': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'education': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'profession': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'student': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'gender': ('Pohlavie'),
            'age': ('Vek'),
            'education': ('Dosiahnuté vzdelanie'),
            'student': ('Ste študent?'),
        }


class PageRatingCreateForm(forms.ModelForm):
    class Meta:
        model = PageRating
        fields = '__all__'
        exclude = ['page', ]
        widgets = {
            'credibility': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'headline_length': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'headline_size': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'font_style': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'font_size': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image_count': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'colors': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'text_length': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'hyperlink_count': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'page_layout': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'credibility': ('Dôveryhodnosť'),
            'headline_length': ('Dĺžka nadpisu'),
            'headline_size': ('Veľkosť nadpisu'),
            'font_style': ('Štýl písma'),
            'font_size': ('Veľkosť písma'),
            'image_count': ('Počet obrázkov'),
            'colors': ('Farby použité na stránke'),
            'text_length': ('Dĺžka textu'),
            'hyperlink_count': ('Počet linkov (hypertextových odkazov)'),
            'page_layout': ('Rozloženie elementov na stránke'),
        }
