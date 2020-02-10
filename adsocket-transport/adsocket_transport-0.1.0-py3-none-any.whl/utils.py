import importlib


def import_driver(name):
    """

    :param pth:
    :return:
    """
    the_module = importlib.import_module(f'adsocket_transport.broker.{name}')
    class_ptr = getattr(the_module, 'broker')

    return class_ptr