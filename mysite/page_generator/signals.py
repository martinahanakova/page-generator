from django.db.models.signals import post_save, pre_save
from django.contrib.sessions.backends.db import SessionStore
from django.dispatch import receiver

from .models import Participant, Page


@receiver(post_save, sender=Participant, dispatch_uid='participant_updated')
def generateParameters(sender, instance, created, **kwargs):
    if not created:
        participant = instance
        order = 1
        headline_size = 1
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


# pridať for cyklus pre generovanie stránok
# rozdeliť do funkcíí
# vytvoriť si pole page_id, ktoré sa bude posielať

# vytvor si novú tabuľku kde k user_id namapujem page_id a pridám ešte round
# tieto page_id si budem postupne vyberať z tabuľky
