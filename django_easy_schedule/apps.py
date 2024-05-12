from django.apps import AppConfig


class DjangoScheduleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_schedule"

    def ready(self):
        import importlib

        from django.conf import settings

        for app in settings.INSTALLED_APPS:
            try:
                importlib.import_module(f"{app}.jobs")
            except ModuleNotFoundError:
                pass
