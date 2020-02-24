import logging

from events.events_manager import EventsManager

logger = logging.getLogger(__name__)


class EventStack:
    eventsManager = EventsManager()

    def __init__(self):
        self.EVENTS_TEST = self.eventsManager.get_event('events.test', 'События.Test', compulsory_reading=True)

        self.EVENTS_PRODUCTION_READY_2_LAUNCH = self.eventsManager.get_event('events.production.ready2Launch', 'События.Производство.Выполнен расчет готовности к запуску', compulsory_reading=False)

        self.EVENTS_PRODUCTION_MAKE_ROUTING = self.eventsManager.get_event('events.planing.route.make', 'События.Планирование.Маршрутизация.Формирование', compulsory_reading=False)
        self.EVENTS_PRODUCTION_DELETE_ROUTING = self.eventsManager.get_event('events.planing.route.delete', 'События.Планирование.Маршрутизация.Удаление', compulsory_reading=False)

        self.EVENTS_PRODUCTION_MAKE_LAUNCH = self.eventsManager.get_event('events.production.launch.make', 'События.Производство.Запуск.Формирование', compulsory_reading=True)
        self.EVENTS_PRODUCTION_DELETE_LAUNCH = self.eventsManager.get_event('events.production.launch.delete', 'События.Производство.Запуск.Удаление', compulsory_reading=True)

        self.EVENTS_PRODUCTION_ORDER_CREATE = self.eventsManager.get_event('events.production.order.create', 'События.Производство.Распоряжение на производство.Формирование', compulsory_reading=True)
        self.EVENTS_PRODUCTION_ORDER_DELETE = self.eventsManager.get_event('events.production.order.delete', 'События.Производство.Распоряжение на производство.Удаление', compulsory_reading=True)

