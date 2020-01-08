"""Module with function to configure dependency injections"""


def config_inject(binder):
    """ Configure dependency injection
    See: https://pypi.org/project/Inject/
    :param binder:
    :return: None
    """
    from django.apps import apps
    for app_config in apps.app_configs.values():
        try:
            providers_cfg = app_config.providers()
        except AttributeError:
            continue
        for interface, impl in providers_cfg:
            binder.bind_to_provider(interface, impl)
