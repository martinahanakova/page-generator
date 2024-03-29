import datetime

from django.db import models
from django.utils import timezone


class Participant(models.Model):

    class GenderChoices(models.TextChoices):
        FEMALE = 'F', 'Žena'
        MALE = 'M', 'Muž'

    class AgeChoices(models.TextChoices):
        TEENS = 'T', '15-19'
        YOUNG = 'Y', '20-24'
        ADULTS_1 = 'A1', '25-34'
        ADULTS_2 = 'A2', '35-44'
        ADULTS_3 = 'A3', '45-54'
        ADULTS_4 = 'A4', '55-64'
        SENIORS = 'S', '65+'

    class EducationChoices(models.TextChoices):
        PRIMARY = '1', 'Základné'
        SECONDARY = '2', 'Stredoškolské bez maturity'
        SECONDARY_M = '3', 'Stredoškolské s maturitou'
        UNIVERSITY = '4', 'Vysokoškolské'
        NONE = '0', 'Žiadne'

    class StudentChoices(models.TextChoices):
        YES = '1', 'Áno'
        NO = '0', 'Nie'

    class ProfessionChoices(models.TextChoices):
        HEALTHCARE = 'H', 'Zdravotníctvo'
        EDUCATION = 'E', 'Školstvo'
        CONSTRUCTION = 'C', 'Stavbeníctvo'
        RESTAURANTS = 'R', 'Reštauračné služby'
        BUSINESS = 'B', 'Podnikanie'
        OTHER = 'O', 'Iné'

    gender = models.CharField(
        max_length=7,
        choices=GenderChoices.choices,
        default=None,
    )
    age = models.CharField(
        max_length=10,
        choices=AgeChoices.choices,
        default=None,
    )
    education = models.CharField(
        max_length=50,
        choices=EducationChoices.choices,
        default=None,
    )
    student = models.CharField(
        max_length=3,
        choices=StudentChoices.choices,
        default=None,
    )
    profession = models.CharField(
        max_length=30,
        choices=ProfessionChoices.choices,
        default="O",
    )
    session_id = models.CharField(max_length=500)


class Page(models.Model):

    class ParameterChoices(models.IntegerChoices):
        CATEGORY_1 = '1'
        CATEGORY_2 = '2'
        CATEGORY_3 = '3'

    class ColorChoices(models.IntegerChoices):
        GROUP_1 = '1'
        GROUP_2 = '2'
        GROUP_3 = '3'
        GROUP_4 = '4'

    class StyleChoices(models.IntegerChoices):
        STYLE_1 = '1'
        STYLE_2 = '2'
        STYLE_3 = '3'
        STYLE_4 = '4'

    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    order = models.IntegerField()
    headline_size = models.IntegerField(
        choices=ParameterChoices.choices,
        default=None,
    )
    font_size = models.IntegerField(
        choices=ParameterChoices.choices,
        default=None,
    )
    font_style = models.IntegerField(
        choices=StyleChoices.choices,
        default=None,
    )
    image_count = models.IntegerField(
        choices=ParameterChoices.choices,
        default=None,
    )
    colors = models.IntegerField(
        choices=ColorChoices.choices,
        default=None,
    )
    text_length = models.IntegerField(
        choices=ParameterChoices.choices,
        default=None,
    )
    hyperlink_count = models.IntegerField(
        choices=ParameterChoices.choices,
        default=None,
    )


class PageRating(models.Model):

    class CredibilityChoices(models.IntegerChoices):
        CREDIBLE_3 = 3, 'Úplne dôveryhodný'
        CREDIBLE_2 = 2, 'Dôveryhodný'
        CREDIBLE_1 = 1, 'Skôr dôveryhodný'
        DONT_KNOW = 0, 'Neviem posúdiť'
        UNCREDIBLE_1 = -1, 'Skôr nedôveryhodný'
        UNCREDIBLE_2 = -2, 'Nedôveryhodný'
        UNCREDIBLE_3 = -3, 'Úplne nedôveryhodný'

    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    credibility = models.IntegerField(
        choices=CredibilityChoices.choices,
        default=None,
    )
    headline_length = models.BooleanField(default=False)
    headline_size = models.BooleanField(default=False)
    font_size = models.BooleanField(default=False)
    font_style = models.BooleanField(default=False)
    image_count = models.BooleanField(default=False)
    colors = models.BooleanField(default=False)
    text_length = models.BooleanField(default=False)
    hyperlink_count = models.BooleanField(default=False)
    page_layout = models.BooleanField(default=False)
    scroll_log = models.TextField(default=None, null=True)
    time_start = models.BigIntegerField(default=0)
    time_end = models.BigIntegerField(default=0)


class Logs(models.Model):

    class LogChoices(models.TextChoices):
        CREDIBILITY_START = 'PS', 'Zobrazenie hodnotenej stránky'
        CREDIBILITY_END = 'CE', 'Odoslanie dotazníka dôveryhodnosti'
        MEDIAL_LITERACY_START = 'MS', 'Začiatok dotazníka mediálnej gramotnosti'

    participant = models.IntegerField()
    page = models.IntegerField(default=None)
    timestamp = models.TextField(
        max_length=50
    )
    log = models.CharField(
        max_length=30,
        choices=LogChoices.choices,
        default=None,
    )



