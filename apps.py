from django.apps import AppConfig


class StellarFouncationConfig(AppConfig):
    name = 'stellar-federation'
    verbose_name = 'Stellar Foundation Sever'

    def ready(self):
        pass
