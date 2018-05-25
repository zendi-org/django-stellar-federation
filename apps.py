from django.apps import AppConfig


class StellarFoundationConfig(AppConfig):
    name = 'stellar_federation'
    verbose_name = 'Stellar Foundation Sever'

    def ready(self):
        pass
