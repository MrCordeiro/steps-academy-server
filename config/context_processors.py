"""Custom context processors"""

from django.conf import settings


def from_settings(request):
    """Makes the variables from settings.py available in the template"""
    return {
        'ENVIRONMENT_NAME': settings.ENVIRONMENT_NAME,
        'ENVIRONMENT_COLOR': settings.ENVIRONMENT_COLOR,
    }