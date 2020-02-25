# Dedicated to the public domain under CC0: https://creativecommons.org/publicdomain/zero/1.0/.

'''
HTML charts.
'''

from functools import reduce
from math import floor, log10
from typing import Any, Callable, Dict, Iterable, Optional, Sequence, Tuple, Union, overload

from ..range import Num, NumRange
from . import Div, HtmlNode, Span, MuAttrs, InlineStyle


Dim = Union[int, float, str]
Vec = Tuple[Num, Num]
VecOrNum = Union[Vec, Num]
F2 = Tuple[float, float]
F2OrF = Union[F2, float]
BoundsF2 = Tuple[F2, F2]
PathCommand = Tuple

PointTransform = Callable[[Tuple], F2]
TickFmt = Callable[[float], Any]
Plotter = Callable[[Div, PointTransform, Any], None]



class ChartSeries:

  name:str
  legend:str
  bounds:Optional[BoundsF2] = None # Overridden by subclasses.

  def render(self, chart:'HtmlChart', container:Div) -> None: raise NotImplementedError



class ChartAxis:

  def __init__(self, *,
   min:Optional[Num]=None, max:Optional[Num]=None,
   visible_origin=False,
   symmetric=False,
   show_grid=True, grid:Iterable[Num]=(), grid_step:Num=0.0, grid_min:Num=16,
   show_ticks=True, ticks:Iterable[Num]=(), tick_step:Num=0.0, tick_space:Num=1,
   tick_w:Num=16, tick_fmt:Optional[TickFmt]=None) -> None:

    self._min = None if min is None else float(min)
    self._max = None if max is None else float(max)
    self.visible_origin = visible_origin
    self.symmetric = symmetric
    self.show_grid = show_grid
    self.grid = list(grid)
    self.grid_step = float(grid_step)
    self.grid_min = float(grid_min)
    self.show_ticks = show_ticks
    self.ticks = list(ticks)
    self.tick_step = float(tick_step)
    self.tick_space = float(tick_space)
    self.tick_w = float(tick_w)
    self.tick_fmt = tick_fmt

    # These attributes are filled in later.
    self.idx = -1
    self.data_len = 0.0
    self.min = 0.0
    self.max = 0.0
    self.transform = _axis_transform_dummy
    self.scale = 0.0

  def calc_min_max(self, data_bounds:Optional[BoundsF2]) -> None:
    # Determine data data_bounds.
    _min:Optional[float] = self._min
    _max:Optional[float] = self._max
    if _min is None: _min = 0.0   if data_bounds is None else data_bounds[0][self.idx]
    if _max is None: _max = _min if data_bounds is None else data_bounds[1][self.idx]
    if _max <= _min: _max = _min + 1.0
    if self.visible_origin:
      if _min > 0.0:   _min = 0.0
      elif _max < 0.0: _max = 0.0
    if self.symmetric:
      _max = max(_max, -_min)
      _min = -_max
    self.min = _min
    self.max = _max

  def calc_layout(self, chart_size:F2, title_h:float, tick_len:float, tick_h:float) -> None:
    self.data_len = self.max - self.min
    self.scale = 1 / self.data_len

    # Calculate tick step.
    tick_min_screen_step = (self.tick_w*1.5) if (self.idx == 0) else (tick_h*2.0)
    tick_mult = 1.0
    frac_w = 0
    fmt_w = 0
    if self.tick_step <= 0 and tick_min_screen_step > 0:
      step1, tick_mult = self.choose_step(tick_min_screen_step)
      self.tick_step = step1 * tick_mult
    if self.tick_step > 0 and not self.tick_fmt:
      exp = floor(log10(self.tick_step))
      frac_w = max(0, -exp)
      fmt_w = max(
        len(f'{self.min:,.{frac_w}f}'),
        len(f'{self.max:,.{frac_w}f}'))

      pad_str = f'{10**fmt_w:,.{frac_w}f}'[-fmt_w:] # Longer than necessary. Take pad chars from right to left.
      def tick_fmt(val:float) -> Any:
        s = f'{val:,.{frac_w}f}'
        return Span(cl='zpad', ch=pad_str[:-len(s)]), s

      self.tick_fmt = tick_fmt

    # Calculate grid step.
    if self.grid_step <= 0:
      step1, mult = self.choose_step(min_screen_step=self.grid_min)
      if mult == 2 and tick_mult == 5: # Ticks will misalign to grid; bump grid to 2.5.
        mult = 2.5
      self.grid_step = step1 * mult

    if self.ticks:
      if not self.grid:
        self.grid = self.ticks
    else: # Calculate ticks.
      ti, tr = divmod(self.min, self.tick_step)
      if tr > 0.1: ti += 1 # If the remainder is visually significant, skip the first tick.
      t_start = ti*self.tick_step
      self.ticks = [t for t in NumRange(t_start, self.max, step=self.tick_step, closed=True)]
      if not self.grid: # Calculate grid.
        g_start = (self.min//self.grid_step + 1) * self.grid_step # Skip line index 0 because it is always <= low border.
        self.grid = [g for g in NumRange(g_start, self.max, self.grid_step)]



  def choose_step(self, min_screen_step:float) -> Tuple[float, float]:
    assert self.data_len > 0
    assert min_screen_step > 0
    axis_length = 100 # TEMP
    cram_num = max(1.0, axis_length // min_screen_step) # Maximum number of ticks that could be placed.
    assert cram_num > 0, (cram_num, axis_length, min_screen_step)
    cram_step = self.data_len / cram_num # Minimum fractional data step.
    exp = floor(log10(cram_step))
    step1 = float(10**exp) # Low estimate of step.
    for mult in (1.0, 2.0, 5.0):
      step = step1 * mult
      if step >= cram_step: return step1, mult
    return step1, 10.0



class HtmlChart(HtmlNode):
  tag = 'div'

  def __init__(self,
   title:str=None,
   x:ChartAxis=None,
   y:ChartAxis=None,
   series:Sequence[ChartSeries]=(),
   symmetric_xy=False,
   dbg=False,
   attrs:MuAttrs=None) -> None:

    attrs = attrs or {}
    super().__init__(attrs=attrs)

    self.prepend_class('chart')
    self.title = title
    self.x = x = ChartAxis() if x is None else x
    self.y = y = ChartAxis() if y is None else y
    self.series = series
    self.symmetric_xy = symmetric_xy

    x.idx = 0
    y.idx = 1

    data_bounds = reduce(expand_opt_bounds, (s.bounds for s in series), None)

    x.calc_min_max(data_bounds=data_bounds)
    y.calc_min_max(data_bounds=data_bounds)

    if symmetric_xy:
      x.min = min(x.min, y.min)
      y.min = x.min
      x.max = max(x.max, y.max)
      y.max = x.max

    # Calculate per-axis length as necessary.
    size = (960,480) # TEMP
    title_h = 14 # TEMP
    tick_len = 48 # TEMP
    tick_h = 16 # TEMP
    x.calc_layout(chart_size=size, title_h=title_h, tick_len=tick_len, tick_h=tick_h)
    y.calc_layout(chart_size=size, title_h=title_h, tick_len=tick_len, tick_h=tick_h)

    self.data_size = data_size = (x.data_len, y.data_len)
    self.grid_size = grid_size = (100, 100) # TEMP
    self.scale = (x.scale, y.scale)

    assert x is not None
    assert y is not None
    ax = x # Hack around mypy.
    ay = y

    def transform(point:Sequence) -> F2:
      'Translate a point to from data space to div space.'
      px = float(point[0])
      py = float(point[1])
      return (round(ax.scale*(px-ax.min), 1), round(ay.scale*(ay.data_len - (py-ay.min)), 1))

    def x_transform(val:Num) -> float: return round(ax.scale*(float(val) - ax.min), 1)
    def y_transform(val:Num) -> float: return round(ay.scale*(ay.data_len - (float(val)-ay.min)), 1)


    self.transform = transform
    x.transform = x_transform
    y.transform = y_transform

    # Contents.

    # Title.
    if self.title is not None:
      self.append(Span(cl='title', ch=self.title))

    area = self.append(Div(cl='chart-area')) # Leave area open.

    # Clip path is is defined to match grid.
    #clip_path_id = area.gen_id()
    #self.chart_clip_path = f'url(#{clip_path_id})'
    #with area.clipPath(id=clip_path_id) as clipPath:
    #  clipPath.rect(size=grid_size, r=corner_radius)

    # Grid.
    if x.show_grid:
      g_start_x = (x.min//x.grid_step + 1) * x.grid_step # Skip line index 0 because it is always <= low border.
      for gx in x.grid: # X axis.
        tgx = x.transform(gx)
        #grid.line((tgx, 0), (tgx, y.length)) # Vertical lines.
    if y.show_grid:
      g_start_y = (y.min//y.grid_step + 1) * y.grid_step # Skip line index 0 because it is always <= low border.
      for gy in y.grid:
        tgy = y.transform(gy)
        #grid.line((0, tgy), (x.length, tgy)) # Horizontal lines.

    # Axes.
    if y.min <= 0 and y.max >= 0: # Draw X axis.
      y0 = y.transform(0)
      #area.line((0, y0), (x.length, y0), cl='axis', id='x-axis')
    if x.min <= 0 and x.max >= 0: # Draw Y axis.
      x0 = x.transform(0)
      #area.line((x0, 0), (x0, y.length), cl='axis', id='y-axis')

    def handle_rendered_tick(val:Any) -> Tuple:
      if isinstance(val, str): return (val,)
      try: return tuple(val)
      except TypeError: return (val,)

    # Ticks.
    if x.show_ticks:
      tick_x = area.append(Div(cl='tick-x'))
      txi, txr = divmod(x.min, x.tick_step)
      if txr > 0.1: txi += 1 # If the remainder is visually significant, skip the first tick.
      t_start_x = txi*x.tick_step
      for _x in x.ticks:
        tx = x.transform(_x)
        ty = 100.0 # TEMP
        tb = ty + tick_len
        tty = tb + x.tick_space
        #tick_x.line((tx, ty), (tx, tb), cl='tick')
        assert x.tick_fmt is not None
        #tick_x.append(Span(ch=str(x.tick_fmt(_x)), pos=(tx, tty), cl='tick'))
    if y.show_ticks:
      tick_y = area.append(Div(cl='tick-y'))
      tyi, tyr = divmod(y.min, y.tick_step)
      if tyr > 0.1: tyi += 1 # If the remainder is visually significant, skip the first tick.
      t_start_y = tyi*y.tick_step
      for _y in y.ticks:
        tx = 100.0 # TEMP
        tr = tx + tick_len
        ttx = tr + y.tick_space
        ty = y.transform(_y)
        #tick_y.line((tx, ty), (tr, ty), cl='tick')
        assert y.tick_fmt is not None
        # tick_y.append(Span(ch=str(y.tick_fmt(_y)), pos=(ttx, ty), cl='tick'))

    # Legend.
    legend_w = 200
    legend_h = 50
    if legend_h > 0:
      leg_y = size[1] - title_h - legend_h - 1
      legend_g = self.append(Div(cl='chart-legend'))
      for i, s in enumerate(series):
        g = legend_g.append(Div(cl='chart-legend-'+s.name, ch=s.legend))


    # Series.
    series_container = area.append(Div(cl='series'))
    for s in series:
      series_div = series_container.append(Div(cl=s.name))
      s.render(self, container=series_div)



class BarSeries(ChartSeries):

  def __init__(self, name:str, points:Sequence[Tuple], numeric:bool, legend:str='', width=1.0, plotter:Optional[Plotter]=None,
   title_fmt:Optional[Callable[[Tuple], str]]=None, **attrs:Any) -> None:

    self.name = name
    self.points = list(points)
    self.numeric = numeric
    self.legend = legend or name
    self.width = width
    self.plotter = plotter
    self.title_fmt = title_fmt
    self.attrs = attrs
    self.bounds:Optional[Tuple[F2, F2]] = None

    def float_from(val:Any, label:str) -> float:
      try: return float(val)
      except TypeError as e: raise TypeError(f'BarSeries received non-numeric point {label}: {val!r}') from e

    if self.points:
      for p in self.points: # Get first value.
        x = p[0]
        y = p[1]
        if numeric:
          x_min = x_max = float_from(x, 'key')
        y_min = y_max = float_from(y, 'value')
        break
      for p in self.points:
        x = p[0]
        y = p[1]
        if numeric:
          x = float_from(x, 'key')
          x_min = min(x_min, x)
          x_max = max(x_max, x)
        y = float_from(y, 'value')
        y_min = min(y_min, y)
        y_max = max(y_max, y)
      if numeric:
        half_w = self.width * 0.5
        self.bounds = ((x_min - half_w, 0.0), (x_max + half_w, y_max))
      else:
        self.bounds = ((0.0, 0.0), (float(len(self.points)), y_max))


  def render(self, chart:'HtmlChart', container:Div) -> None:
    assert self.plotter is None # TODO
    w = chart.x.scale * self.width
    # Do not place the bars in a group because we want to be able to z-index bars across multiple series.
    for i, p in enumerate(self.points):
      if not self.numeric:
        p = (i+0.5, p[1], p[0])
      (x_mid, y) = chart.transform(p)
      assert p[1] >= 0, f'negative bar values are not yet supported: {p!r}'
      kwargs:Dict[str,Any] = {}
      if self.title_fmt:
        kwargs['title'] = self.title_fmt(p)
      left = x_mid - w*0.5
      right = x_mid + w*0.5
      bottom = 0
      top = y
      style = InlineStyle(
        left=f'{left:.3%}',
        right=f'{right:.3%}',
        bottom=f'{bottom:.3%}',
        top=f'{top:.3%}',
        z_index=i)
      container.append(Div(style=style, **kwargs, **self.attrs)) # TODO: Custom format of title?



def _axis_transform_dummy(val:Num) -> float: raise Exception('missing transform')
def scale(x:Num=1, y:Num=1) -> str: return f'scale({x},{y})'
def rotate(degrees:Num, x:Num=0, y:Num=0) -> str: return f'rotate({fmt_num(degrees)},{fmt_num(x)},{fmt_num(y)})'
def translate(x:Num=0, y:Num=0) -> str: return f'translate({fmt_num(x)},{fmt_num(y)})'


@overload
def fmt_num(n:Num) -> str: ...
@overload
def fmt_num(n:None) -> None: ...

def fmt_num(n:Optional[Num]) -> Optional[str]:
  'Remove trailing ".0" from floats that can be represented as integers.'
  if n is None: return None
  if isinstance(n, float):
    i = int(n)
    if i == n: return str(i)
  return str(n)


def f2_for_vec(v:Vec) -> F2:
  x, y = v
  return (float(x), float(y))


def unpack_VecOrNum(vn:VecOrNum) -> Tuple[float, float]:
  if isinstance(vn, tuple):
    x, y = vn
    return float(x), float(y)
  else:
    s = float(vn)
    return (s, s)


def expand_opt_bounds(l:Optional[BoundsF2], r:Optional[BoundsF2]) -> Optional[BoundsF2]:
  if l is None: return r
  if r is None: return l
  (llx, lly), (lhx, lhy) = l
  (rlx, rly), (rhx, rhy) = r
  return ((min(llx, rlx), min(lly, rly)), (max(lhx, rhx), max(lhy, rhy)))


chart_style = '''
.chart {
  background-color: red;
  width: 100%;
  height: 16rem;
}
.chart > .chart-legend {
  background-color: blue;
}
.chart > div.chart-area {
  background-color: yellow;
  width: 100%;
  height: 100%;
}
.chart .series {
  position: relative;
  background-color: green;
}

.chart .series div {
  position: absolute;
}

text {
  stroke: none;
  fill: currentColor;
}
text.title {
  text-anchor: start;
  alignment-baseline: hanging;
}
g.tick-x text.tick {
  white-space: pre;
  text-anchor: start;
  alignment-baseline: hanging;
}
g.tick-y text.tick {
  white-space: pre;
  text-anchor: start;
  alignment-baseline: alphabetic;
}
g.chart-legend text {
  text-anchor: start;
  alignment-baseline: central;
}
'''
