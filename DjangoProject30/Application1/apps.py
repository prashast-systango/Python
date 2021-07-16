from django.apps import AppConfig


class Application1Config(AppConfig):
    name = 'Application1'

    def ready(self):
        import Application1.signals