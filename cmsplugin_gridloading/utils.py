from django.conf import settings


def get_additional_styles():
    """
    Get additional effect choices from settings
    """
    choices = []
    raw = getattr(settings, 'GRIDLOADING_EFFECT', False)
    if raw:
        if isinstance(raw, basestring):
            raw = raw.split(',')
        for choice in raw:
            clean = choice.strip()
            choices.append((clean.lower(), clean.title()))
    return choices