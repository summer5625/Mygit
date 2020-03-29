from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class Web1Config(AppConfig):
    name = 'web1'

    def ready(self):
        autodiscover_modules('stark')
