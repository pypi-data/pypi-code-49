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

class Plot:
    def __init__(self, title='plot'):
        self.title = title
        self.points = []
        self.x_min =  math.inf
        self.x_max = -math.inf
        self.y_min =  math.inf
        self.y_max = -math.inf

    def point(self, x, y, r=0, g=0, b=0, a=1):
        y = -y
        self.points.append([x, y, r, g, b, a])
        self.x_min = min(x, self.x_min)
        self.x_max = max(x, self.x_max)
        self.y_min = min(y, self.y_min)
        self.y_max = max(y, self.y_max)

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
        view = [self.x_min, self.y_min, self.x_max-self.x_min, self.y_max-self.y_min]
        media.view_set(*view)
        def move(view, dx, dy):
            view[0] -= dx*view[2]/media.width()
            view[1] -= dy*view[3]/media.height()
            media.view_set(*view)
        def zoom(view, zx, zy, x, y):
            # change view so (x, y) stays put and (w, h) multiplies by (zx, zy)
            new_view_w = view[2]*zx
            new_view_h = view[3]*zy
            view[0] += x/media.width () * (view[2] - new_view_w)
            view[1] += y/media.height() * (view[3] - new_view_h)
            view[2] = new_view_w
            view[3] = new_view_h
            media.view_set(*view)
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
            self.vertex_buffer.draw()
            margin_x = 2.0 / media.width()  * view[2]
            margin_y = 2.0 / media.height() * view[3]
            ## x axis
            i = view[0] + view[2] / 8
            while i < view[0] + 15 * view[2] / 16:
                s = '{:.8}'.format(i)
                media.vector_text(s, x=i+margin_x, y=view[1]+view[3]-margin_y, h=8.0/media.height()*view[3])
                media.line(xi=i, xf=i, y=view[1]+view[3], h=-12.0/media.height()*view[2])
                i += view[2] / 8
            ## y axis
            i = view[1] + view[3] / 8
            while i < view[1] + 15 * view[3] / 16:
                s = '{:.8}'.format(-i)
                media.vector_text(s, x=view[0]+margin_x, y=i-margin_y, h=8.0/media.height()*view[3])
                media.line(x=view[0], w=12.0/media.width()*view[2], yi=i, yf=i)
                i += view[3] / 8
            ## display
            media.display()
            media.capture_finish('plot.png')

    def _construct(self):
        self.vertex_buffer = media.VertexBuffer(len(self.points))
        for i, point in enumerate(self.points):
            self.vertex_buffer.update(i, *point)

def _default_transform(x, y, series=0):
    colors = [
        (255, 255, 255),
        (255,   0,   0),
        (  0, 255,   0),
        (  0,   0, 255),
        (255, 255,   0),
        (  0, 255, 255),
        (255,   0, 255),
    ]
    return (x, y, *colors[series%len(colors)], 255)

def plot_list(l, transform=_default_transform, title='plot'):
    plot = Plot(title)
    for i, v in enumerate(l):
        plot.point(*transform(i, v))
    plot.show()

def plot_lists(ls, transform=_default_transform, title='plot'):
    plot = Plot(title)
    for j, l in enumerate(ls):
        for i, v in enumerate(l):
            plot.point(*transform(i, v, j))
    plot.show()

def plot_scatter(x, y, transform=_default_transform, title='plot'):
    plot = Plot(title)
    for i in range(min(len(x), len(y))):
        plot.point(*transform(x[i], y[i]))
    plot.show()

def plot_scatter_xs(xs, y, transform=_default_transform, title='plot'):
    plot = Plot(title)
    for j, x in enumerate(xs):
        for i in range(min(len(x), len(y))):
            plot.point(*transform(x[i], y[i], j))
    plot.show()

def plot_scatter_ys(x, ys, transform=_default_transform, title='plot'):
    plot = Plot(title)
    for j, y in enumerate(ys):
        for i in range(min(len(x), len(y))):
            plot.point(*transform(x[i], y[i], j))
    plot.show()

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

def plot(*args, transform=_default_transform, title='plot'):
    plot_func = None
    if len(args) == 1:
        if   _is_dim(args[0], 1): plot_func = plot_list
        elif _is_dim(args[0], 2): plot_func = plot_lists
    elif len(args) == 2:
        if   _is_dim(args[0], 1) and _is_dim(args[1], 1): plot_func = plot_scatter
        elif _is_dim(args[0], 2) and _is_dim(args[1], 1): plot_func = plot_scatter_xs
        elif _is_dim(args[0], 1) and _is_dim(args[1], 2): plot_func = plot_scatter_ys
    if not plot_func:
        raise Exception('unknown plot type for argument types {}'.format([type(i) for i in args]))
    return plot_func(*args, transform=transform, title=title)
