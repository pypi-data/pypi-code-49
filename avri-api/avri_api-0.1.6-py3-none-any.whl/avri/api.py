from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

import requests
from functional import seq

BASE_URL = ('https://dataservice.deafvalapp.nl/dataservice/DataServiceServlet'
            '?service={service}'
            '&land={country_code}'
            '&postcode={postal_code}'
            '&huisnr={house_nr}'
            '&huisnrtoev={house_nr_extension}'
            )

SCHEDULE = 'OPHAALSCHEMA'

CACHE_LIMIT_DAYS = 6


@dataclass(frozen=True)
class Garbage:
    name: str
    day: datetime


@dataclass(frozen=True)
class Cache:
    data: List[Garbage]
    date: datetime


class AvriException(Exception):
    pass


class Avri:
    def __init__(self, postal_code: str,
                 house_nr: str,
                 house_nr_extension: Optional[str] = None,
                 country_code='NL'):
        if not house_nr_extension:
            house_nr_extension = ''
        self.postal_code = self.clean_postal_code(postal_code)
        self.house_nr = house_nr
        self.house_nr_extension = house_nr_extension
        self.country_code = country_code

        self._cache: Optional[Cache] = None

    @staticmethod
    def clean_postal_code(pc: str):
        return pc.replace(" ", "")

    def _should_recache(self):
        return not self._cache or (datetime.now() - self._cache.date).days > CACHE_LIMIT_DAYS

    def get_data(self):
        if self._should_recache():
            data = self.perform_request()
            if not data:
                raise AvriException(f'No data found for {self.postal_code} {self.house_nr}, {self.country_code}')
            self._cache = Cache(self.parse_content(data), datetime.now())
        return self._cache.data

    def perform_request(self):
        try:
            return (requests.get(BASE_URL.format(service=SCHEDULE,
                                                 country_code=self.country_code,
                                                 postal_code=self.postal_code,
                                                 house_nr=self.house_nr,
                                                 house_nr_extension=self.house_nr_extension))
                    .content
                    .decode()
                    )
        except Exception as e:
            raise AvriException("Something went wrong contacting the Avri API") from e

    @staticmethod
    def parse_content(content: str):
        def parse_row(row):
            fields = row.split(';')
            name = fields[0]
            collect_days = [datetime.strptime(_, '%d-%m-%Y') for _ in fields[1:] if _ != '']
            yield from [Garbage(name.lower(), day) for day in collect_days]

        return (seq(content.split('\n'))
                .flat_map(parse_row))

    @staticmethod
    def today_midnight():
        return datetime.combine(datetime.now(), datetime.min.time())

    def upcoming(self, dt: datetime = None):
        if not dt:
            dt = self.today_midnight()
        data = self.get_data()
        return (seq(data)
                .filter(lambda g: g.day >= dt)
                .sorted(lambda g: g.day)
                .first()
                )

    def upcoming_of_each(self, dt: datetime = None):
        if not dt:
            dt = self.today_midnight()
        data = self.get_data()
        return (seq(data)
                .filter(lambda g: g.day >= dt)
                .sorted(lambda g: g.day)
                .map(lambda g: (g.name, g.day))
                .reduce_by_key(lambda x, y: min(x, y))
                .map(lambda arg: Garbage(*arg))
                .list()
                )

    def all_upcoming(self):
        data = self.get_data()
        return (seq(data)
                .filter(lambda g: g.day >= datetime.now())
                .sorted(lambda g: g.day)
                .list()
                )
