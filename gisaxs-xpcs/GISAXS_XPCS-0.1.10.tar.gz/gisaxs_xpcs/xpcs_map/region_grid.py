# -*- coding: utf-8 -*-
from typing import Union, Tuple, NamedTuple

RegionType = Tuple[float, float, float, float]
RegionTypeShort = Tuple[float, float]


class RListParams(NamedTuple):
    init_window: Union[RegionType, RegionTypeShort]
    step: float
    axis: int
    number_of_cuts: int
    mode: str = 'list'

    @property
    def dict(self) -> dict:
        return self._asdict()


class RGridParams(NamedTuple):
    init_window: Union[RegionType, RegionTypeShort]
    xy_step: Tuple[float, float]
    xy_size: Tuple[int, int]
    mode: str = 'grid'

    @property
    def dict(self) -> dict:
        return self._asdict()


def r_params_from_dict(params: dict) -> Union[RListParams, RGridParams]:
    try:
        mode = params.pop('mode')
    except KeyError:
        raise KeyError('Mode key is missing.')
    if mode == 'list':
        try:
            return RListParams(**params)
        except TypeError:
            raise KeyError(f'Some arguments are missing: {params}')
    elif mode == 'grid':
        try:
            return RGridParams(**params)
        except TypeError:
            raise KeyError(f'Some arguments are missing: {params}')
    else:
        raise ValueError(f'Unknown mode {mode}.')


class RegionGrid(list):
    """
    RegionGrid is a list containing elements
    of type Tuple[x_min, x_max, y_min, y_max].
    x_min, x_max, y_min, y_max are values in degrees
    that define a window on a GISAXS image within which
    XPCS correlation functions will be calculated.

    Should be only initialized via classmethods and never from __init__().
    """

    __slots__ = ['parameters']

    @classmethod
    def get_cut_list(cls, init_window: Union[RegionType, RegionTypeShort],
                     axis: int, step: float, number_of_cuts: int):
        self = cls()
        if axis not in (0, 1):
            raise ValueError('Axis value should be 0 (cuts along q parallel)'
                             ' or 1 (cuts along q z axis)')
        if len(init_window) == 2:
            init_window = (init_window[0], init_window[0] + step,
                           init_window[1], init_window[1] + step)
        if axis == 0:
            self.append([(init_window[0] + step * i,
                          init_window[1] + step * i,
                          init_window[2],
                          init_window[3]) for i in range(number_of_cuts)])
        else:
            self.append([(init_window[0],
                          init_window[1],
                          init_window[2] + step * i,
                          init_window[3] + step * i)
                         for i in range(number_of_cuts)])
        setattr(self, 'parameters', RListParams(init_window=init_window, step=step,
                                                axis=axis, number_of_cuts=number_of_cuts,
                                                mode='list'))
        return self

    @classmethod
    def get_cut_grid(cls, init_window: Union[RegionType, RegionTypeShort],
                     xy_step: Tuple[float, float],
                     xy_size: Tuple[int, int]):
        if len(init_window) == 2:
            init_window = (init_window[0], init_window[0] + xy_step[0],
                           init_window[1], init_window[1] + xy_step[1])
        self = cls()
        for i in range(xy_size[0]):
            for j in range(xy_size[1]):
                self.append((init_window[0] + xy_step[0] * i,
                             init_window[1] + xy_step[0] * i,
                             init_window[2] + xy_step[1] * j,
                             init_window[3] + xy_step[1] * j))
        setattr(self, 'parameters', RGridParams(init_window=init_window, xy_step=xy_step,
                                                xy_size=xy_size, mode='grid'))
        return self

    @classmethod
    def init_from_parameters_dict(cls, parameters: Union[dict, RListParams, RGridParams]):
        if isinstance(parameters, (RListParams, RGridParams)):
            parameters = parameters.dict
        try:
            mode = parameters.pop('mode')
            if mode == 'grid':
                return cls.get_cut_grid(**parameters)
            elif mode == 'list':
                return cls.get_cut_list(**parameters)
            else:
                raise ValueError('Mode should be "grid" or "list".')

        except TypeError as err:
            raise KeyError('Provided parameters dict does not contain'
                           ' necessary parameter. Error: %s ' % err)

    def get_ranges(self) -> dict:
        def func(i):
            return [x[i] for x in self]

        x_range = (min(func(0)), max(func(1)))
        y_range = (min(func(2)), max(func(3)))
        return dict(x_range=x_range, y_range=y_range)

    def __repr__(self):
        return f'<RegionGrid: {self.parameters}\n' \
            f'Values:{super().__repr__()}>'
