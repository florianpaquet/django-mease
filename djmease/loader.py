from django.conf import settings
from django.utils.importlib import import_module


def autodiscover():
    """
    Autodiscovers apps with `mease_registry` modules
    """
    for app in getattr(settings, 'INSTALLED_APPS', []):
        import_module(app)

        try:
            import_module('%s.mease_registry' % app)
        except ImportError:
            pass
