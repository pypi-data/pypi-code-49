"Python class definitions for SQL INTERVAL types that are based on SECOND"
from __future__ import annotations

from typing import List, Dict
from datetime import timedelta
from ..util import MetaInfo, mk_nullable, ValConv, ValConvMaker

def split_secs(secs: int, num_splits: int) -> List[int]:
	s = []
	for div in [60, 60, 24][:num_splits-1]:
		s.insert(0, secs % div)
		secs //= div
	s.insert(0, secs)
	return s

def split_to_num(s: str) -> List[float]:
	return [float(x) for x in s.split(':')]

class SecondsDelta(timedelta):
	def __init__(self, *args, **kwargs):
		self.scale = 6 - next(a for a in range(6, -1, -1) if self.microseconds % 10**a == 0)

	def set_scale(self, scale: int) -> SecondsDelta:
		self.scale = scale
		return self

	def __str__(self):
		s = ('-' if self.days < 0 else ' ') + self._abs_str(abs(self.days * 86400 + self.seconds))
		if self.scale > 0:
			s += '.' + format(self.microseconds, '06d')[:self.scale]
		return s

	def sqlrepr(self) -> str:
		s = str(self)
		sign, val = s[0].rstrip(), s[1:]
		return f"INTERVAL {sign}'{val}' {self._sql_type}"

	__repr__ = sqlrepr

	@classmethod
	def mk_conv_fn(cls, m: MetaInfo) -> ValConv:
		def parse(s: str):
			return cls.parse(s, m["Scale"])
		return mk_nullable(parse) if m["MayBeNull"] else parse

	@classmethod
	def _abs_str(cls, v: int) -> str:
		raise NotImplementedError()

	@classmethod
	def _parse_val(cls, s: str) -> timedelta:
		raise NotImplementedError()

	@classmethod
	def parse(cls, s: str, scale: int = 0) -> SecondsDelta:
		v = -1 * cls._parse_val(s[1:]) if s[0] == '-' else cls._parse_val(s.lstrip())
		return cls(days=v.days, seconds=v.seconds, microseconds=v.microseconds).set_scale(scale)

class Second(SecondsDelta):
	_sql_type = 'SECOND'

	@classmethod
	def _abs_str(cls, v: int) -> str:
		return str(v)

	@classmethod
	def _parse_val(cls, s: str) -> timedelta:
		return timedelta(seconds=float(s))

class Minute(SecondsDelta):
	_sql_type = 'MINUTE'

	@classmethod
	def _abs_str(cls, v: int) -> str:
		return str(v // 60)

	@classmethod
	def _parse_val(cls, s: str) -> timedelta:
		return timedelta(minutes=int(s))

class MinuteToSecond(SecondsDelta):
	_sql_type = 'MINUTE TO SECOND'

	@classmethod
	def _abs_str(cls, v: int) -> str:
		m, s = split_secs(v, 2)
		return f"{m}:{s:02d}"

	@classmethod
	def _parse_val(cls, s: str) -> timedelta:
		m, s = split_to_num(s)
		return timedelta(minutes=m, seconds=s)

class Hour(SecondsDelta):
	_sql_type = 'HOUR'

	@classmethod
	def _abs_str(cls, v: int) -> str:
		return str(v // 3600)

	@classmethod
	def _parse_val(cls, s: str) -> timedelta:
		return timedelta(hours=int(s))

class HourToMinute(SecondsDelta):
	_sql_type = 'HOUR TO MINUTE'

	@classmethod
	def _abs_str(cls, v: int) -> str:
		h, m, _ = split_secs(v, 3)
		return f"{h}:{m:02d}"

	@classmethod
	def _parse_val(cls, s: str) -> timedelta:
		h, m = split_to_num(s)
		return timedelta(hours=h, minutes=m)

class HourToSecond(SecondsDelta):
	_sql_type = 'HOUR TO SECOND'

	@classmethod
	def _abs_str(cls, v: int) -> str:
		h, m, s = split_secs(v, 3)
		return f"{h}:{m:02d}:{s:02d}"

	@classmethod
	def _parse_val(cls, s: str) -> timedelta:
		h, m, s = split_to_num(s)
		return timedelta(hours=h, minutes=m, seconds=s)

class Day(SecondsDelta):
	_sql_type = 'DAY'

	@classmethod
	def _abs_str(cls, v: int) -> str:
		return str(v // 86400)

	@classmethod
	def _parse_val(cls, s: str) -> timedelta:
		return timedelta(days=int(s))

class DayToHour(SecondsDelta):
	_sql_type = 'DAY TO HOUR'

	@classmethod
	def _abs_str(cls, v: int) -> str:
		d, h, *_ = split_secs(v, 4)
		return f"{d} {h:02d}"

	@classmethod
	def _parse_val(cls, s: str) -> timedelta:
		d, h = s.split(' ')
		return timedelta(days=int(d), hours=int(h))

class DayToMinute(SecondsDelta):
	_sql_type = 'DAY TO MINUTE'

	@classmethod
	def _abs_str(cls, v: int) -> str:
		d, h, m, _ = split_secs(v, 4)
		return f"{d} {h:02d}:{m:02d}"

	@classmethod
	def _parse_val(cls, s: str) -> timedelta:
		d, tm = s.split(' ')
		h, m = split_to_num(tm)
		return timedelta(days=int(d), hours=h, minutes=m)

class DayToSecond(SecondsDelta):
	_sql_type = 'DAY TO SECOND'

	@classmethod
	def _abs_str(cls, v: int) -> str:
		d, h, m, s = split_secs(v, 4)
		return f"{d} {h:02d}:{m:02d}:{s:02d}"

	@classmethod
	def _parse_val(cls, s: str) -> timedelta:
		d, tm = s.split(' ')
		h, m, s = split_to_num(tm)
		return timedelta(days=int(d), hours=h, minutes=m, seconds=s)

def register_conv_fn() -> Dict[str, ValConvMaker]:
	all_classes = [Second, Minute, MinuteToSecond, Hour, HourToMinute, HourToSecond, Day, DayToHour, DayToMinute, DayToSecond]
	return {'INTERVAL ' + cls._sql_type : cls.mk_conv_fn for cls in all_classes}
