import math
import os
import re
import sys

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(DIR, 'danssfml', 'wrapper'))

try:
    import media
except:
    from danssfmlpy import media

class View:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def tuple(self): return [self.x, self.y, self.w, self.h]

class Plot:
    def __init__(self, title='plot', transform=None):
        self.title = title
        self.points = []
        self.lines = []
        self.texts = []
        self.x_min =  math.inf
        self.x_max = -math.inf
        self.y_min =  math.inf
        self.y_max = -math.inf
        self.series = 0
        def default_transform(x, y, i, series):
            colors = [
                (255, 255, 255),
                (255,   0,   0),
                (  0, 255,   0),
                (  0,   0, 255),
                (255, 255,   0),
                (  0, 255, 255),
                (255,   0, 255),
            ]
            color = colors[series%len(colors)]
            return {
                'x': x, 'y': y,
                'r': color[0], 'g': color[1], 'b': color[2],
                'a': 255,
            }
        self.transform = transform or default_transform

    def point(self, x, y, r=0, g=0, b=0, a=255):
        y = -y
        self.points.append([x, y, r, g, b, a])
        self._include(x, y)

    def line(self, xi, yi, xf, yf, r=0, g=0, b=0, a=255):
        yi = -yi
        yf = -yf
        self.lines.append([xi, yi, xf, yf, r, g, b, a])
        self._include(xi, yi)
        self._include(xf, yf)

    def text(self, s, x, y, r=0, g=0, b=0, a=255):
        y = -y
        self.texts.append([s, x, y, r, g, b, a])
        self._include(x, y)

    def show(self, w=640, h=480):
        media.init(w, h, title=self.title)
        media.custom_resize(True)
        dragging = False
        mouse = [0, 0]
        if self.x_min == self.x_max:
            self.x_min -= 1
            self.x_max += 1
        if self.y_min == self.y_max:
            self.y_min -= 1
            self.y_max += 1
        dx = self.x_max - self.x_min
        dy = self.y_max - self.y_min
        self.x_min -= dx / 16
        self.y_min -= dy / 16
        self.x_max += dx / 16
        self.y_max += dy / 16
        view = View(self.x_min, self.y_min, self.x_max-self.x_min, self.y_max-self.y_min)
        media.view_set(*view.tuple())
        def move(view, dx, dy):
            view.x -= dx*view.w/media.width()
            view.y -= dy*view.h/media.height()
            media.view_set(*view.tuple())
        def zoom(view, zx, zy, x, y):
            # change view so (x, y) stays put and (w, h) multiplies by (zx, zy)
            new_view_w = view.w*zx
            new_view_h = view.h*zy
            view.x += x/media.width () * (view.w - new_view_w)
            view.y += y/media.height() * (view.h - new_view_h)
            view.w = new_view_w
            view.h = new_view_h
            media.view_set(*view.tuple())
        self._construct()
        while True:
            # handle events
            while True:
                event = media.poll_event()
                if not event: break
                # quit
                if event == 'q':
                    media.close()
                    return
                # resize
                m = re.match(r'rw(\d+)h(\d+)', event)
                if m:
                    w, h = (int(i) for i in m.groups())
                    zoom(view, w/media.width(), h/media.height(), w/2, h/2)
                    continue
                # left mouse button
                if event[0] == 'b':
                    dragging = {'<': True, '>': False}[event[1]]
                    if dragging:
                        m = re.match(r'b<0x(\d+)y(\d+)', event)
                        drag_prev = (int(i) for i in m.groups())
                    continue
                # mouse move
                m = re.match(r'x(\d+)y(\d+)', event)
                if m:
                    mouse = [int(i) for i in m.groups()]
                    if dragging:
                        xi, yi = drag_prev
                        dx, dy = mouse[0]-xi, mouse[1]-yi
                        move(view, dx, dy)
                        drag_prev = mouse
                    continue
                # mouse wheel
                if event.startswith('w'):
                    delta = int(event[1:])
                    z = 1.25 if delta > 0 else 0.8
                    zoom(view, z, z, mouse[0], mouse[1])
                # keyboard
                m = re.match('<(.+)', event)
                if m:
                    key = m.group(1)
                    moves = {
                        'Left' : ( 10,   0),
                        'Right': (-10,   0),
                        'Up'   : (  0,  10),
                        'Down' : (  0, -10),
                    }
                    if key in moves:
                        move(view, *moves[key])
                        continue
                    zooms = {
                        'a': (1.25, 1),
                        'd': (0.80, 1),
                        'w': (1, 1.25),
                        's': (1, 0.80),
                    }
                    if key in zooms:
                        zoom(view, *zooms[key], media.width()/2, media.height()/2)
                        continue
                    if key == 'Return': media.capture_start()
            # draw
            media.clear(color=(0, 0, 0))
            for i in self.vertex_buffers: i.draw()
            margin_x = 2.0 / media.width()  * view.w
            margin_y = 2.0 / media.height() * view.h
            aspect = media.height() / media.width() * view.w / view.h
            text_h = 10.0/media.height()*view.h
            ## texts
            for (s, x, y, r, g, b, a) in self.texts:
                media.vector_text(s, x=x, y=y-text_h/4, h=text_h, aspect=aspect, r=r, g=g, b=b, a=a)
                media.line(x=x, y=y, w=text_h, h=0, r=r, g=g, b=b, a=a)
            ## x axis
            x_divs = media.width() // 200
            i = view.x + view.w / x_divs
            while i < view.x + (x_divs*2-1) * view.w / (x_divs*2):
                s = '{:.8}'.format(i)
                media.vector_text(s, x=i+margin_x, y=view.y+view.h-margin_y, h=text_h, aspect=aspect)
                media.line(xi=i, xf=i, y=view.y+view.h, h=-12.0/media.height()*view.h)
                i += view.w / x_divs
            ## y axis
            y_divs = media.height() // 80
            i = view.y + view.h / y_divs
            while i < view.y + (y_divs*2-1) * view.h / (y_divs*2):
                s = '{:.8}'.format(-i)
                media.vector_text(s, x=view.x+margin_x, y=i-margin_y, h=text_h, aspect=aspect)
                media.line(x=view.x, w=12.0/media.width()*view.w, yi=i, yf=i)
                i += view.h / y_divs
            ## display
            media.display()
            media.capture_finish('plot.png')

    def plot_list(self, l):
        for i, v in enumerate(l):
            self.point(**self.transform(i, v, i, self.series))
        self.series += 1

    def plot_lists(self, ls):
        for l in ls: self.plot_list(l)

    def plot_scatter(self, x, y):
        for i in range(min(len(x), len(y))):
            self.point(**self.transform(x[i], y[i], i, self.series))
        self.series += 1

    def plot_scatter_xs(self, xs, y):
        for x in xs: self.plot_scatter(x, y)

    def plot_scatter_ys(self, x, ys):
        for y in ys: self.plot_scatter(x, y)

    def plot_dict(self, d):
        for x, y in d.items():
            self.point(**self.transform(x, y, i, self.series))
        self.series += 1

    def plot_dicts(self, ds):
        for d in ds: self.plot_dict(d)

    def plot_f(self, f, x=(-1, 1), steps=100):
        args_prev = None
        for i in range(steps):
            x_curr = x[0] + (x[1]-x[0]) * i/(steps-1)
            y_curr = f(x_curr)
            args_curr = self.transform(x_curr, y_curr, i, self.series)
            if args_prev: self.line(
                xi=args_prev['x'], yi=args_prev['y'],
                xf=args_curr['x'], yf=args_curr['y'],
                r=args_prev['r'], g=args_prev['g'], b=args_prev['b'], a=args_prev['a'],
            )
            args_prev = args_curr
        self.series += 1

    def plot(self, *args, **kwargs):
        plot_func = None
        if len(args) == 1:
            if   _is_dim(args[0], 1): plot_func = self.plot_list
            elif _is_dim(args[0], 2): plot_func = self.plot_lists
            elif type(args[0]) == dict: plot_func = self.plot_dict
            elif _type_r(args[0]) == _type_r([{}]): plot_func = self.plot_dicts
            elif callable(args[0]): plot_func = self.plot_f
        elif len(args) == 2:
            if   _is_dim(args[0], 1) and _is_dim(args[1], 1): plot_func = self.plot_scatter
            elif _is_dim(args[0], 2) and _is_dim(args[1], 1): plot_func = self.plot_scatter_xs
            elif _is_dim(args[0], 1) and _is_dim(args[1], 2): plot_func = self.plot_scatter_ys
        if not plot_func:
            raise Exception('unknown plot type for argument types {}'.format([type(i) for i in args]))
        plot_func(*args, **kwargs)
        return self

    def _construct(self):
        # points
        points = media.VertexBuffer(len(self.points))
        for i, point in enumerate(self.points):
            points.update(i, *point)
        # lines
        lines = media.VertexBuffer(2*len(self.lines))
        lines.set_type('lines')
        for i, (xi, yi, xf, yf, r, g, b, a) in enumerate(self.lines):
            lines.update(2*i+0, xi, yi, r, g, b, a)
            lines.update(2*i+1, xf, yf, r, g, b, a)
        # order
        self.vertex_buffers = [lines, points]

    def _include(self, x, y):
        self.x_min = min(x, self.x_min)
        self.x_max = max(x, self.x_max)
        self.y_min = min(y, self.y_min)
        self.y_max = max(y, self.y_max)

def plot(*args, title='plot'):
    Plot(title).plot(*args).show()

def _type_r(v, max_depth=None, _depth=0):
    if type(v) in [int, float]: return 'number'
    if max_depth != None and _depth == max_depth:
        return str(type(v))
    try:
        v[0]
        return '{}({})'.format(type(v), _type_r(v[0], max_depth, _depth+1))
    except:
        return str(type(v))

def _is_dim(v, dim):
    u = 0
    for i in range(dim): u = [u]
    return _type_r(v, dim) == _type_r(u)
