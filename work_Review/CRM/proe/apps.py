from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class ProeConfig(AppConfig):
    name = 'proe'

    def ready(self):
        autodiscover_modules('stark')