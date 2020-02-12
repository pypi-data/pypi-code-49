from typing import Dict, Iterable, Union, Tuple
from datetime import datetime, date
import logging

logger = logging.getLogger(__name__)


def add_inflation_multiple(index_map: Dict, rows: Iterable[Tuple[Union[float, int], date]], to: date = None, discounting_rate: float = 1.06):
    ix_current = next(iter(index_map.values()))

    vals = []

    to = datetime.now().date() if to is None else to

    for v, dt in rows:

        if isinstance(dt, datetime):
            dt = datetime.date()

        d = dt.replace(day=1)  # type: date

        if d > to:
            delta = d - to
            full_years = int(delta.days / 365)
            vals.append(
                v / (discounting_rate ** full_years)
            )
            continue

        ix_past = index_map.get(d.strftime('%Y-%m-%d'))

        if ix_past is None:
            logger.warning(f'No inflation index value for date "{d.strftime("%Y-%m")}"')
            vals.append(v)
            continue

        vals.append(
            v * ix_current / ix_past
        )

    return vals


def add_inflation_single(index_map: Dict, amount: Union[float, int], dt: date, to: date = None, discounting_rate: float = 1.06):
    if isinstance(dt, str):
        dt = datetime.strptime(dt, '%Y-%m-%d').date()
    return add_inflation_multiple(index_map, [(amount, dt), ], to, discounting_rate)[0]
