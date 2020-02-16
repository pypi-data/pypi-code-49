"""
# [kollavarsham](http://kollavarsham.org/)

[![NPM version](https://badge.fury.io/js/kollavarsham.svg)](https://badge.fury.io/js/kollavarsham) [![PyPI version](https://badge.fury.io/py/kollavarsham.svg)](https://badge.fury.io/py/kollavarsham) [![Build Status](https://img.shields.io/travis/kollavarsham/kollavarsham-js.svg)](https://travis-ci.org/kollavarsham/kollavarsham-js) [![Dependency Status](https://img.shields.io/david/kollavarsham/kollavarsham-js.svg)](https://david-dm.org/kollavarsham/kollavarsham-js) [![Dev-Dependency Status](https://img.shields.io/david/dev/kollavarsham/kollavarsham-js.svg)](https://david-dm.org/kollavarsham/kollavarsham-js#info=devDependencies&view=table) [![Coverage Status](https://coveralls.io/repos/github/kollavarsham/kollavarsham-js/badge.svg?branch=master)](https://coveralls.io/github/kollavarsham/kollavarsham-js?branch=master)

> Convert Gregorian date to Kollavarsham date and vice versa

## Install

```sh
$ npm install --save kollavarsham
```

## Usage

```js
import { Kollavarsham } from 'kollavarsham';

const options = {
  system: 'SuryaSiddhanta',
  latitude: 10,
  longitude: 76.2
};

const kollavarsham = new Kollavarsham(options);

const todayInMalayalamEra = kollavarsham.fromGregorianDate(new Date());

const today = kollavarsham.toGregorianDate(todayInMalayalamEra);
```

## Documentation

Check out the [Kollavarsham class](https://kollavarsham.org/kollavarsham-js/module-kollavarsham.Kollavarsham.html) within the API documentation as this is the entry point into the library.

## CLI app

Check out the [cli](https://www.npmjs.com/package/kollavarsham-cli) module ([GitHub repo](https://github.com/kollavarsham/cli)) for the `kollavarsham` cross-platform CLI app

```plain
npm install -g kollavarsham-cli

kollavarsham --help
```

## Release History

Check out the history at [GitHub Releases](https://github.com/kollavarsham/kollavarsham-js/releases)

## License

Copyright (c) 2014-2020 The Kollavarsham Team. Licensed under the [MIT license](http://kollavarsham.org/LICENSE.txt).
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

__jsii_assembly__ = jsii.JSIIAssembly.load("kollavarsham", "1.6.3", __name__, "kollavarsham@1.6.3.jsii.tgz")


class BaseDate(metaclass=jsii.JSIIAbstractClass, jsii_type="kollavarsham.BaseDate"):
    """Serves as the base class for both the {@link JulianDate} and {@link KollavarshamDate} classes.

    **INTERNAL/PRIVATE**

    class:
    :class:: BaseDate
    constructor:
    :constructor:: true
    """
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _BaseDateProxy

    def __init__(self, year: typing.Optional[jsii.Number]=None, month: typing.Optional[jsii.Number]=None, date: typing.Optional[jsii.Number]=None) -> None:
        """
        :param year: -
        :param month: -
        :param date: -
        """
        jsii.create(BaseDate, self, [year, month, date])

    @jsii.member(jsii_name="getMasaName")
    @builtins.classmethod
    def get_masa_name(cls, masa_number: jsii.Number) -> "MasaName":
        """Returns the month names object that has Saka, Saura and Kollavarsham (English & Malayalam) month names for the specified index ``masaNumber``.

        :param masa_number: -

        for:
        :for:: BaseDate
        method:
        :method:: getMasaName
        """
        return jsii.sinvoke(cls, "getMasaName", [masa_number])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> str:
        """Converts the Date to a nicely formatted string with year, month and date.

        for:
        :for:: BaseDate
        method:
        :method:: toString
        type:
        :type:: {string}
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property
    @jsii.member(jsii_name="mlWeekdayName")
    def ml_weekday_name(self) -> str:
        """Returns the weekday (in Malayalam) for the current instance of date.

        property:
        :property:: mlWeekdayName
        type:
        :type:: {string}
        """
        return jsii.get(self, "mlWeekdayName")

    @builtins.property
    @jsii.member(jsii_name="sauraMasaName")
    def saura_masa_name(self) -> str:
        """Returns the Saura Masa name for the current instance of date.

        property:
        :property:: sauraMasaName
        type:
        :type:: {string}
        """
        return jsii.get(self, "sauraMasaName")

    @builtins.property
    @jsii.member(jsii_name="weekdayName")
    def weekday_name(self) -> str:
        """Returns the weekday (in English) for the current instance of date.

        property:
        :property:: weekdayName
        type:
        :type:: {string}
        """
        return jsii.get(self, "weekdayName")

    @builtins.property
    @jsii.member(jsii_name="ahargana")
    def ahargana(self) -> jsii.Number:
        """The ``Ahargana`` corresponding to this instance of the date. **Set separately after an instance is created**.

        In Sanskrit ``ahoratra`` means one full day and ``gana`` means count.
        Hence, the Ahargana on any given day stands for the number of lunar days that have elapsed starting from an epoch.

        *Source*: http://cs.annauniv.edu/insight/Reading%20Materials/astro/sharptime/ahargana.htm

        property:
        :property:: ahargana
        type:
        :type:: {Number}
        """
        return jsii.get(self, "ahargana")

    @ahargana.setter
    def ahargana(self, value: jsii.Number):
        jsii.set(self, "ahargana", value)

    @builtins.property
    @jsii.member(jsii_name="date")
    def date(self) -> jsii.Number:
        """The date corresponding to this instance of the date.

        property:
        :property:: date
        type:
        :type:: {Number}
        """
        return jsii.get(self, "date")

    @date.setter
    def date(self, value: jsii.Number):
        jsii.set(self, "date", value)

    @builtins.property
    @jsii.member(jsii_name="gregorianDate")
    def gregorian_date(self) -> datetime.datetime:
        """The gregorian date corresponding to this instance of the date.

        **Set separately after an instance is created**

        property:
        :property:: gregorianDate
        type:
        :type:: {Date}
        """
        return jsii.get(self, "gregorianDate")

    @gregorian_date.setter
    def gregorian_date(self, value: datetime.datetime):
        jsii.set(self, "gregorianDate", value)

    @builtins.property
    @jsii.member(jsii_name="julianDay")
    def julian_day(self) -> jsii.Number:
        """The ``Julian Day`` corresponding to this instance of the date.

        **Set separately after an instance is created**
        Julian day is the continuous count of days since the beginning of the Julian Period used primarily by astronomers.

        *Source*: https://en.wikipedia.org/wiki/Julian_day

        property:
        :property:: julianDay
        type:
        :type:: {Number}
        """
        return jsii.get(self, "julianDay")

    @julian_day.setter
    def julian_day(self, value: jsii.Number):
        jsii.set(self, "julianDay", value)

    @builtins.property
    @jsii.member(jsii_name="month")
    def month(self) -> jsii.Number:
        """The month corresponding to this instance of the date.

        property:
        :property:: month
        type:
        :type:: {Number}
        """
        return jsii.get(self, "month")

    @month.setter
    def month(self, value: jsii.Number):
        jsii.set(self, "month", value)

    @builtins.property
    @jsii.member(jsii_name="naksatra")
    def naksatra(self) -> "Naksatra":
        return jsii.get(self, "naksatra")

    @naksatra.setter
    def naksatra(self, value: "Naksatra"):
        jsii.set(self, "naksatra", value)

    @builtins.property
    @jsii.member(jsii_name="sauraDivasa")
    def saura_divasa(self) -> jsii.Number:
        """The ``Saura Divasa`` (Solar Calendar Day) for this instance of the date.

        **Set separately after an instance is created**

        property:
        :property:: sauraDivasa
        type:
        :type:: {Number}
        """
        return jsii.get(self, "sauraDivasa")

    @saura_divasa.setter
    def saura_divasa(self, value: jsii.Number):
        jsii.set(self, "sauraDivasa", value)

    @builtins.property
    @jsii.member(jsii_name="sauraMasa")
    def saura_masa(self) -> jsii.Number:
        """The ``Saura Masa`` (Solar Calendar Month) for this instance of the date.

        **Set separately after an instance is created**

        property:
        :property:: sauraMasa
        type:
        :type:: {Number}
        """
        return jsii.get(self, "sauraMasa")

    @saura_masa.setter
    def saura_masa(self, value: jsii.Number):
        jsii.set(self, "sauraMasa", value)

    @builtins.property
    @jsii.member(jsii_name="year")
    def year(self) -> jsii.Number:
        """The year corresponding to this instance of the date.

        property:
        :property:: year
        type:
        :type:: {Number}
        """
        return jsii.get(self, "year")

    @year.setter
    def year(self, value: jsii.Number):
        jsii.set(self, "year", value)


class _BaseDateProxy(BaseDate):
    pass

class JulianDate(BaseDate, metaclass=jsii.JSIIMeta, jsii_type="kollavarsham.JulianDate"):
    """Represents a Julian date's year, month and day ``toGregorianDateFromSaka`` method of the {@link Kollavarsham} class returns an instance of this type for dates older than ``1st January 1583 AD``.

    **INTERNAL/PRIVATE**

    class:
    :class:: JulianDate
    constructor:
    :constructor:: true
    extends:
    :extends:: BaseDate
    """
    def __init__(self, year: typing.Optional[jsii.Number]=None, month: typing.Optional[jsii.Number]=None, day: typing.Optional[jsii.Number]=None) -> None:
        """
        :param year: -
        :param month: -
        :param day: -
        """
        jsii.create(JulianDate, self, [year, month, day])


class Kollavarsham(metaclass=jsii.JSIIMeta, jsii_type="kollavarsham.Kollavarsham"):
    """The Kollavarsham class implements all the public APIs of the library.

    Create a new instance of this class, passing in the relevant options and call methods on the instance.

    class:
    :class:: Kollavarsham
    constructor:
    :constructor:: true

    Example::

        # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
        Kollavarsham = require("kollavarsham")
        
        options = {
            "system": "SuryaSiddhanta",
            "latitude": 10,
            "longitude": 76.2
        }
        
        kollavarsham = Kollavarsham(options)
        
        today_in_malayalam_era = kollavarsham.from_gregorian_date(Date())
        
        today = kollavarsham.to_gregorian_date(today_in_malayalam_era)
    """
    def __init__(self, *, latitude: jsii.Number, longitude: jsii.Number, system: str) -> None:
        """
        :param latitude: 
        :param longitude: 
        :param system: 
        """
        options = Settings(latitude=latitude, longitude=longitude, system=system)

        jsii.create(Kollavarsham, self, [options])

    @jsii.member(jsii_name="fromGregorianDate")
    def from_gregorian_date(self, date: datetime.datetime) -> "KollavarshamDate":
        """Converts a Gregorian date to the equivalent Kollavarsham date, respecting the current configuration.

        :param date: The Gregorian date to be converted to Kollavarsham.

        return
        :return: Converted date

        for:
        :for:: Kollavarsham
        method:
        :method:: fromGregorianDate

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            Kollavarsham = require("Kollavarsham")
            kollavarsham = Kollavarsham()
            today = kollavarsham.from_gregorian_date(Date(1979, 4, 22))
        """
        return jsii.invoke(self, "fromGregorianDate", [date])

    @jsii.member(jsii_name="toGregorianDate")
    def to_gregorian_date(self, date: "KollavarshamDate") -> datetime.datetime:
        """Converts a Kollavarsham date (an instance of {@link kollavarshamDate}) to its equivalent Gregorian date, respecting the current configuration.

        This method Will return {@link JulianDate} object for any date before 1st January 1583 AD and
        `Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`_ objects for later dates.

        **This API has not been implemented yet**

        :param date: The Kollavarsham date to be converted to Gregorian.

        return
        :return: Converted date

        for:
        :for:: Kollavarsham
        method:
        :method:: toGregorianDate
        throws:
        :throws:: *"When the API is implemented, will convert <date>"**
        """
        return jsii.invoke(self, "toGregorianDate", [date])

    @jsii.member(jsii_name="toGregorianDateFromSaka")
    def to_gregorian_date_from_saka(self, saka_date: "SakaDate") -> "KollavarshamDate":
        """Converts a Saka date (an instance of {@link sakaDate}) to its equivalent Gregorian date, respecting the current configuration.

        This method Will return {@link JulianDate} object for any date before 1st January 1583 AD and
        `Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`_ objects for later dates.

        :param saka_date: The Saka date to be converted to Gregorian.

        return
        :return: Converted date

        for:
        :for:: Kollavarsham
        method:
        :method:: toGregorianDateFromSaka
        """
        return jsii.invoke(self, "toGregorianDateFromSaka", [saka_date])

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> "Settings":
        return jsii.get(self, "settings")

    @settings.setter
    def settings(self, value: "Settings"):
        jsii.set(self, "settings", value)


class KollavarshamDate(BaseDate, metaclass=jsii.JSIIMeta, jsii_type="kollavarsham.KollavarshamDate"):
    """Represents a Kollavarsham date's year, month and date.

    class:
    :class:: KollavarshamDate
    constructor:
    :constructor:: true
    extends:
    :extends:: BaseDate
    """
    def __init__(self, year: typing.Optional[jsii.Number]=None, month: typing.Optional[jsii.Number]=None, day: typing.Optional[jsii.Number]=None) -> None:
        """
        :param year: -
        :param month: -
        :param day: -
        """
        jsii.create(KollavarshamDate, self, [year, month, day])

    @builtins.property
    @jsii.member(jsii_name="masaName")
    def masa_name(self) -> str:
        """Returns the Kollavarsham month name (in English) for this instance of date.

        property:
        :property:: masaName
        type:
        :type:: {string}
        """
        return jsii.get(self, "masaName")

    @builtins.property
    @jsii.member(jsii_name="mlMasaName")
    def ml_masa_name(self) -> str:
        """Returns the Kollavarsham month name (in Malayalam) for this instance of date.

        property:
        :property:: mlMasaName
        type:
        :type:: {string}
        """
        return jsii.get(self, "mlMasaName")

    @builtins.property
    @jsii.member(jsii_name="mlNaksatraName")
    def ml_naksatra_name(self) -> str:
        """Returns the Kollavarsham Naksatra name (in Malayalam) for this instance of date.

        property:
        :property:: mlNaksatraName
        type:
        :type:: {string}
        """
        return jsii.get(self, "mlNaksatraName")

    @builtins.property
    @jsii.member(jsii_name="naksatraName")
    def naksatra_name(self) -> str:
        """Returns the Kollavarsham Naksatra name (in English) for this instance date.

        property:
        :property:: naksatraName
        type:
        :type:: {string}
        """
        return jsii.get(self, "naksatraName")

    @builtins.property
    @jsii.member(jsii_name="sakaDate")
    def saka_date(self) -> "SakaDate":
        return jsii.get(self, "sakaDate")

    @saka_date.setter
    def saka_date(self, value: "SakaDate"):
        jsii.set(self, "sakaDate", value)


@jsii.data_type(jsii_type="kollavarsham.MasaName", jsii_struct_bases=[], name_mapping={'en_malayalam': 'enMalayalam', 'ml_malayalam': 'mlMalayalam', 'saka': 'saka', 'saura': 'saura'})
class MasaName():
    def __init__(self, *, en_malayalam: str, ml_malayalam: str, saka: str, saura: str):
        """
        :param en_malayalam: 
        :param ml_malayalam: 
        :param saka: 
        :param saura: 
        """
        self._values = {
            'en_malayalam': en_malayalam,
            'ml_malayalam': ml_malayalam,
            'saka': saka,
            'saura': saura,
        }

    @builtins.property
    def en_malayalam(self) -> str:
        return self._values.get('en_malayalam')

    @builtins.property
    def ml_malayalam(self) -> str:
        return self._values.get('ml_malayalam')

    @builtins.property
    def saka(self) -> str:
        return self._values.get('saka')

    @builtins.property
    def saura(self) -> str:
        return self._values.get('saura')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'MasaName(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="kollavarsham.Naksatra", jsii_struct_bases=[], name_mapping={'en_malayalam': 'enMalayalam', 'ml_malayalam': 'mlMalayalam', 'saka': 'saka'})
class Naksatra():
    def __init__(self, *, en_malayalam: str, ml_malayalam: str, saka: str):
        """
        :param en_malayalam: 
        :param ml_malayalam: 
        :param saka: 
        """
        self._values = {
            'en_malayalam': en_malayalam,
            'ml_malayalam': ml_malayalam,
            'saka': saka,
        }

    @builtins.property
    def en_malayalam(self) -> str:
        return self._values.get('en_malayalam')

    @builtins.property
    def ml_malayalam(self) -> str:
        return self._values.get('ml_malayalam')

    @builtins.property
    def saka(self) -> str:
        return self._values.get('saka')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'Naksatra(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class SakaDate(BaseDate, metaclass=jsii.JSIIMeta, jsii_type="kollavarsham.SakaDate"):
    """Represents an Saka date's year, month and paksa and tithi.

    class:
    :class:: SakaDate
    constructor:
    :constructor:: true
    extends:
    :extends:: BaseDate
    """
    def __init__(self, year: typing.Optional[jsii.Number]=None, month: typing.Optional[jsii.Number]=None, tithi: typing.Optional[jsii.Number]=None, paksa: typing.Optional[str]=None) -> None:
        """
        :param year: -
        :param month: -
        :param tithi: -
        :param paksa: -
        """
        jsii.create(SakaDate, self, [year, month, tithi, paksa])

    @jsii.member(jsii_name="generateKollavarshamDate")
    def generate_kollavarsham_date(self) -> "KollavarshamDate":
        """Generates an instance of {@link KollavarshamDate} from this instance of SakaDate.

        for:
        :for:: SakaDate
        method:
        :method:: generateKollavarshamDate
        """
        return jsii.invoke(self, "generateKollavarshamDate", [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> str:
        """Converts the Date to a nicely formatted string with year, month and date."""
        return jsii.invoke(self, "toString", [])

    @builtins.property
    @jsii.member(jsii_name="masaName")
    def masa_name(self) -> str:
        """Returns the month name for this instance of SakaDate.

        property:
        :property:: masaName
        type:
        :type:: {string}
        """
        return jsii.get(self, "masaName")

    @builtins.property
    @jsii.member(jsii_name="naksatraName")
    def naksatra_name(self) -> str:
        """Returns the Saka Naksatra name for this instance of SakaDate.

        property:
        :property:: naksatraName
        type:
        :type:: {string}
        """
        return jsii.get(self, "naksatraName")

    @builtins.property
    @jsii.member(jsii_name="sakaYear")
    def saka_year(self) -> jsii.Number:
        """Returns the Saka year on this instance of SakaDate (same as the underlyiung ``year`` property from the {@link BaseDate} class).

        property:
        :property:: sakaYear
        type:
        :type:: {Number}
        """
        return jsii.get(self, "sakaYear")

    @builtins.property
    @jsii.member(jsii_name="tithi")
    def tithi(self) -> jsii.Number:
        """Returns the Tithi on this instance of SakaDate (same as the underlyiung ``date`` property from the {@link BaseDate} class).

        In Vedic timekeeping, a tithi (also spelled thithi) is a lunar day, or the time it takes for the longitudinal angle between the Moon and the Sun to increase by 12°.
        Tithis begin at varying times of day and vary in duration from approximately 19 to approximately 26 hours.

        *Source*: https://en.wikipedia.org/wiki/Tithi

        property:
        :property:: tithi
        type:
        :type:: {Number}
        """
        return jsii.get(self, "tithi")

    @builtins.property
    @jsii.member(jsii_name="vikramaYear")
    def vikrama_year(self) -> jsii.Number:
        """Returns the Vikrama year corresponding to the Saka year of this instance.

        property:
        :property:: vikramaYear
        type:
        :type:: {Number}
        """
        return jsii.get(self, "vikramaYear")

    @builtins.property
    @jsii.member(jsii_name="adhimasa")
    def adhimasa(self) -> str:
        """The Adhimasa (``Adhika Masa``) prefix corresponding to this instance of the date.

        **Set separately after an instance is created**

        property:
        :property:: adhimasa
        type:
        :type:: {string}
        """
        return jsii.get(self, "adhimasa")

    @adhimasa.setter
    def adhimasa(self, value: str):
        jsii.set(self, "adhimasa", value)

    @builtins.property
    @jsii.member(jsii_name="fractionalTithi")
    def fractional_tithi(self) -> jsii.Number:
        """The fractional ``Tithi``corresponding to this instance of the date.

        **Set separately after an instance is created**

        property:
        :property:: fractionalTithi
        type:
        :type:: {Number}
        """
        return jsii.get(self, "fractionalTithi")

    @fractional_tithi.setter
    def fractional_tithi(self, value: jsii.Number):
        jsii.set(self, "fractionalTithi", value)

    @builtins.property
    @jsii.member(jsii_name="kaliYear")
    def kali_year(self) -> jsii.Number:
        """The Kali year corresponding to this instance of the date.

        **Set separately after an instance is created**

        property:
        :property:: kaliYear
        type:
        :type:: {Number}
        """
        return jsii.get(self, "kaliYear")

    @kali_year.setter
    def kali_year(self, value: jsii.Number):
        jsii.set(self, "kaliYear", value)

    @builtins.property
    @jsii.member(jsii_name="originalAhargana")
    def original_ahargana(self) -> jsii.Number:
        """The original ahargana passed in to the celestial calculations (TODO: Not sure why we need this!?)."""
        return jsii.get(self, "originalAhargana")

    @original_ahargana.setter
    def original_ahargana(self, value: jsii.Number):
        jsii.set(self, "originalAhargana", value)

    @builtins.property
    @jsii.member(jsii_name="paksa")
    def paksa(self) -> str:
        """The Paksha/Paksa corresponding to this instance of the date.

        Paksha (or pakṣa: Sanskrit: पक्ष), refers to a fortnight or a lunar phase in a month of the Hindu lunar calendar.

        *Source*: https://en.wikipedia.org/wiki/Paksha

        property:
        :property:: paksa
        type:
        :type:: {string}
        """
        return jsii.get(self, "paksa")

    @paksa.setter
    def paksa(self, value: str):
        jsii.set(self, "paksa", value)

    @builtins.property
    @jsii.member(jsii_name="sunriseHour")
    def sunrise_hour(self) -> jsii.Number:
        """The hour part from the sunrise time for this date.

        **Set separately after an instance is created**

        property:
        :property:: sunriseHour
        type:
        :type:: {Number}
        """
        return jsii.get(self, "sunriseHour")

    @sunrise_hour.setter
    def sunrise_hour(self, value: jsii.Number):
        jsii.set(self, "sunriseHour", value)

    @builtins.property
    @jsii.member(jsii_name="sunriseMinute")
    def sunrise_minute(self) -> jsii.Number:
        """The minute part from the sunrise time for this date.

        **Set separately after an instance is created**

        property:
        :property:: sunriseMinute
        type:
        :type:: {Number}
        """
        return jsii.get(self, "sunriseMinute")

    @sunrise_minute.setter
    def sunrise_minute(self, value: jsii.Number):
        jsii.set(self, "sunriseMinute", value)


@jsii.data_type(jsii_type="kollavarsham.Settings", jsii_struct_bases=[], name_mapping={'latitude': 'latitude', 'longitude': 'longitude', 'system': 'system'})
class Settings():
    def __init__(self, *, latitude: jsii.Number, longitude: jsii.Number, system: str):
        """
        :param latitude: 
        :param longitude: 
        :param system: 
        """
        self._values = {
            'latitude': latitude,
            'longitude': longitude,
            'system': system,
        }

    @builtins.property
    def latitude(self) -> jsii.Number:
        return self._values.get('latitude')

    @builtins.property
    def longitude(self) -> jsii.Number:
        return self._values.get('longitude')

    @builtins.property
    def system(self) -> str:
        return self._values.get('system')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'Settings(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["BaseDate", "JulianDate", "Kollavarsham", "KollavarshamDate", "MasaName", "Naksatra", "SakaDate", "Settings", "__jsii_assembly__"]

publication.publish()
