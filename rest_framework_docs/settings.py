from django.conf import settings


class DRFSettings(object):

    def __init__(self):
        self.drf_settings = {
            "HIDE_DOCS": self.get_setting("HIDE_DOCS") or False
        }

    def __getitem__(self, item):
        return self.settings[item]

    def get_setting(self, name, default):
        try:
            return settings.REST_FRAMEWORK_DOCS[name]
        except (KeyError, AttributeError):
            return default

    @property
    def settings(self):
        return self.drf_settings


drf_settings = DRFSettings()
