from django.apps import AppConfig


class MyblockConfig(AppConfig):
    name = 'myblock'

    def ready(self):
        from . import signals