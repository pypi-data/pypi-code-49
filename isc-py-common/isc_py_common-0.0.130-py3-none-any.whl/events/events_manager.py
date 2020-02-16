import logging

from django.db import transaction

from isc_common.bit import IsBitOn, TurnBitOn

logger = logging.getLogger(__name__)


class Event:
    event_type = None
    bot = None

    def __init__(self, **kwargs):
        from events.models.event_types import Event_types
        from events.models.event_type_users import Event_type_users

        for k, v in kwargs.items():
            setattr(self, k, v() if callable(v) else v)

        if not isinstance(self.event_type, Event_types):
            raise Exception(f'Not specified "event_type"')

        self.users = [event_type_users.user for event_type_users in Event_type_users.objects.filter(event_type=self.event_type)]

    def send_message(self, message):
        from isc_common.auth.http.LoginRequets import LoginRequest
        from tracker.models.messages import MessagesManager
        from events.models.event_type_users import Event_type_usersManager

        for user in self.users:
            LoginRequest.send_bot_message(
                user=user,
                bot=Event_type_usersManager.get_bot(self.event_type),
                message=f'<h3>Сообщение от:</h3> #{self.event_type.full_name}'
                        f'<p>{MessagesManager.get_border(message, user)}',
                compulsory_reading=IsBitOn(self.event_type.props, 1)
            )


class EventsManager:
    events = []

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v() if callable(v) else v)

    def get_event(self, code, name, compulsory_reading=True) -> Event:
        from events.models.event_types import Event_types

        events = [event for event in self.events if event.event_type.code == code]
        if len(events) == 0:
            with transaction.atomic():
                if not isinstance(code, str):
                    raise Exception(f'Not specified "code" event')

                if not isinstance(name, str):
                    raise Exception(f'Not specified "code" event')

                codes = code.split('.')
                names = name.split('.')

                if len(codes) != len(names):
                    raise Exception(f'Not mapping "code" to "name')

                code_path = None
                index = 0
                parent = None
                event = None
                for _code in codes:
                    if code_path == None:
                        code_path = f'{_code}'
                    else:
                        code_path = f'{code_path}.{_code}'

                    props = 0
                    if index == len(codes) - 1:
                        props = TurnBitOn(props, 0)
                        if compulsory_reading:
                            props = TurnBitOn(props, 1)

                    event_type, _ = Event_types.objects.update_or_create(
                        code=code_path,
                        defaults=dict(
                            name=names[index],
                            props=props,
                            parent=parent,
                            editing=False,
                            deliting=False,
                        )
                    )

                    if IsBitOn(event_type.props, 0):
                        event = Event(event_type=event_type)
                        self.events.append(event)

                    index += 1
                    parent = event_type
                return event
        else:
            return events[0]
