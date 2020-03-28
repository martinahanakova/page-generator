from django.db.models.signals import post_save
from django.db.models import Count, Q
from django.contrib.sessions.backends.db import SessionStore
from django.dispatch import receiver

from .models import Participant, Page

import numpy as np
import math


@receiver(post_save, sender=Participant, dispatch_uid='participant_updated')
def generateParameters(sender, instance, created, **kwargs):
    if not created:
        participant = instance
        order = 1
        headline_size = 3
        font_size = 2
        font_style = 3
        image_count = 3
        colors = 2
        text_length = 1
        hyperlink_count = 2

        page = Page(participant=participant,
            order=order,
            headline_size=headline_size,
            font_size=font_size,
            font_style=font_style,
            image_count=image_count,
            colors=colors,
            text_length=text_length,
            hyperlink_count=hyperlink_count)

        page.save()


def generate(participant, parameter):

    if particpant.age == "T" or particpant.age == "Y":
        age = "A1"
    elif participant.age == "A4" or particpant.age == "S":
        age = "A3"
    else:
        age = "A2"

    if particpant.education == "4":
        education = "E3"
    elif particpant.education == "3" or particpant.education == "2":
        education = "E2"
    else:
        education = "E1"

    student = particpant.student

    ageProbability = getProbability(age, parameter)
    educationProbability = getProbability(education, parameter)
    studentProbability = getProbability(student, parameter)

    # postupne prejdem polia a vždy vynásobím spolu tie čo sú na rovnakom mieste
    # prenormujem tak, že spočítam všetky prvky v poli a potom každý prvok vydelím vypočítaným súčtom

    # následne numpy.random.choice  (pravdepodobnosti)

    # dorobiť for cyklus


def getProbability(category, parameter):

    if category == "A1":
        parameter_counts = Page.objects.values(parameter).\
        filter(participant__in=Participant.objects.filter(Q(age='T') | Q(age='Y'))).\
        annotate(Count(parameter))
    if category == "A2":
        parameter_counts = Page.objects.values(parameter).\
        filter(participant__in=Participant.objects.filter(Q(age='A1') | Q(age='A2') | Q(age='A3'))).\
        annotate(Count(parameter))
    if category == "A3":
        parameter_counts = Page.objects.values(parameter).\
        filter(participant__in=Participant.objects.filter(Q(age='A4') | Q(age='S'))).\
        annotate(Count(parameter))
    if category == "E1":
        parameter_counts = Page.objects.values(parameter).\
        filter(participant__in=Participant.objects.filter(Q(education='0') | Q(education='1'))).\
        annotate(Count(parameter))
    if category == "E2":
        parameter_counts = Page.objects.values(parameter).\
        filter(participant__in=Participant.objects.filter(Q(education='2') | Q(education='3'))).\
        annotate(Count(parameter))
    if category == "E3":
        parameter_counts = Page.objects.values(parameter).\
        filter(participant__in=Participant.objects.filter(Q(education='4'))).\
        annotate(Count(parameter))
    if category:
        parameter_counts = Page.objects.values(parameter).\
        filter(participant__in=Participant.objects.filter(Q(student=True))).\
        annotate(Count(parameter))
    else:
        parameter_counts = Page.objects.values(parameter).\
        filter(participant__in=Participant.objects.filter(Q(student=False))).\
        annotate(Count(parameter))


    sum = 0
    probabilities = []

    for value in parameter_counts:
    sum = sum + value[parameter + '__count']

    for value in parameter_counts:
    probabilities.append(round(abs((value[parameter + '__count'] / sum) - 1), 2))

    array_sum = math.fsum(probabilities)
    probabilities = np.array(probabilities)
    normalized = probabilities / array_sum

    return normalized
