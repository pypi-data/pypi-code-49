import ctypes
import glob
import os
import pprint
import sys

HOME=os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(HOME, '..', 'deps', 'obvious'))

import obvious

sfml=obvious.load_lib('DansSfmlWrapper', [
	'.',
	'built',
	os.path.join('..', 'built'),
	HOME,
	os.path.join(HOME, '..', '..', 'built'),
])
def set_ffi_types(ff, restype=None, *argtypes):
	conversions={
		int: ctypes.c_int,
		float: ctypes.c_float,
		str: ctypes.c_char_p,
		'void*': ctypes.c_void_p,
	}
	ff.restype=conversions.get(restype, restype)
	ff.argtypes=[conversions.get(i, i) for i in argtypes]
set_ffi_types(sfml.dans_sfml_wrapper_init, int, int, int, str)
set_ffi_types(sfml.dans_sfml_wrapper_close)
set_ffi_types(sfml.dans_sfml_wrapper_poll_event, str)
set_ffi_types(sfml.dans_sfml_wrapper_vertices_set_type, None, str)
set_ffi_types(sfml.dans_sfml_wrapper_vertices_add, None, float, float, int, int, int, int)
set_ffi_types(sfml.dans_sfml_wrapper_vertices_draw)
set_ffi_types(sfml.dans_sfml_wrapper_vertex_buffer_construct, 'void*', int)
set_ffi_types(sfml.dans_sfml_wrapper_vertex_buffer_destruct, None, 'void*')
set_ffi_types(sfml.dans_sfml_wrapper_vertex_buffer_update, None, 'void*', int, float, float, int, int, int, int)
set_ffi_types(sfml.dans_sfml_wrapper_vertex_buffer_draw, None, 'void*')
set_ffi_types(sfml.dans_sfml_wrapper_text_draw, None, float, float, int, str, int, int, int, int)
set_ffi_types(sfml.dans_sfml_wrapper_text_width, float, int, str)
set_ffi_types(sfml.dans_sfml_wrapper_width, int)
set_ffi_types(sfml.dans_sfml_wrapper_height, int)
set_ffi_types(sfml.dans_sfml_wrapper_display)
set_ffi_types(sfml.dans_sfml_wrapper_view_get_x, float)
set_ffi_types(sfml.dans_sfml_wrapper_view_get_y, float)
set_ffi_types(sfml.dans_sfml_wrapper_view_get_width, float)
set_ffi_types(sfml.dans_sfml_wrapper_view_get_height, float)
set_ffi_types(sfml.dans_sfml_wrapper_view_set, None, float, float, float, float)
set_ffi_types(sfml.dans_sfml_wrapper_custom_resize, None, int)
set_ffi_types(sfml.dans_sfml_wrapper_capture_start, None)
set_ffi_types(sfml.dans_sfml_wrapper_capture_finish, None, str)
set_ffi_types(sfml.dans_sfml_wrapper_vector_text, None, float, float, float, str, int, int, int, int)
set_ffi_types(sfml.dans_sfml_wrapper_render_texture_construct, 'void*', int, int)
set_ffi_types(sfml.dans_sfml_wrapper_render_texture_destruct, None, 'void*')
set_ffi_types(sfml.dans_sfml_wrapper_render_texture_draw, None, 'void*', float, float, float, float)
set_ffi_types(sfml.dans_sfml_wrapper_render_texture_as_target, 'void*', 'void*')
set_ffi_types(sfml.dans_sfml_wrapper_render_texture_display, None, 'void*')
set_ffi_types(sfml.dans_sfml_wrapper_target_set, None, 'void*')
set_ffi_types(sfml.dans_sfml_wrapper_target_reset)
def init(width=640, height=480, title=''):
	assert sfml.dans_sfml_wrapper_init(width, height, title.encode())==0

def close():
	sfml.dans_sfml_wrapper_close()

def set_sfml(new_sfml):
	global sfml
	sfml=new_sfml
	sfml.dans_sfml_wrapper_poll_event.restype=ctypes.c_char_p

set_sfml(sfml)

def poll_event(): return sfml.dans_sfml_wrapper_poll_event().decode()
def vertices_set_type(s): sfml.dans_sfml_wrapper_vertices_set_type(s.encode())
def vertices_add(x, y, r, g, b, a): sfml.dans_sfml_wrapper_vertices_add(x, y, r, g, b, a)
def vertices_draw(): sfml.dans_sfml_wrapper_vertices_draw()
def width(): return sfml.dans_sfml_wrapper_width()
def height(): return sfml.dans_sfml_wrapper_height()
def display(): sfml.dans_sfml_wrapper_vertices_draw(); sfml.dans_sfml_wrapper_display()
def view_get(): return (
	sfml.dans_sfml_wrapper_view_get_x(),
	sfml.dans_sfml_wrapper_view_get_y(),
	sfml.dans_sfml_wrapper_view_get_width(),
	sfml.dans_sfml_wrapper_view_get_height(),
)
def view_set(x, y, w, h): sfml.dans_sfml_wrapper_view_set(x, y, w, h)
def custom_resize(enable): sfml.dans_sfml_wrapper_custom_resize(1 if enable else 0)

def _xi_yi(**kwargs):
	if 'bounds' in kwargs:
		xi, yi, xf, yf=kwargs['bounds']
	if 'xi' in kwargs:
		xi=kwargs['xi']
		xf=kwargs['xf']
	if 'yi' in kwargs:
		yi=kwargs['yi']
		yf=kwargs['yf']
	if 'x' in kwargs:
		xi=kwargs['x']
		xf=xi+kwargs['w']
	if 'y' in kwargs:
		yi=kwargs['y']
		yf=yi+kwargs['h']
	if kwargs.get('right', False):
		d=xf-xi
		xi-=d
		xf-=d
	if kwargs.get('bottom', False):
		d=yf-yi
		yi-=d
		yf-=d
	if kwargs.get('middle_x', False):
		d=(xf-xi)/2
		xi-=d
		xf-=d
	if kwargs.get('middle_y', False):
		d=(yf-yi)/2
		yi-=d
		yf-=d
	return (xi, yi, xf, yf)

def _color(**kwargs):
	r=kwargs.get('r', 255)
	g=kwargs.get('g', 255)
	b=kwargs.get('b', 255)
	a=kwargs.get('a', 255)
	c=kwargs.get('color', ())
	if   len(c)==3: r, g, b   =c
	elif len(c)==4: r, g, b, a=c
	return (r, g, b, a)

def text(s, **kwargs):
	kwargs['xf']=0
	kwargs['w' ]=0
	xi, yi, xf, yf=_xi_yi(**kwargs)
	r, g, b, a=_color(**kwargs)
	sfml.dans_sfml_wrapper_text_draw(xi, yi, int(round(yf-yi+0.5)), s.encode(), r, g, b, a)

def fill(**kwargs):
	vertices_set_type('triangles')
	xi, yi, xf, yf=_xi_yi(**kwargs)
	r, g, b, a=_color(**kwargs)
	vertices_add(xi, yi, r, g, b, a)
	vertices_add(xf, yi, r, g, b, a)
	vertices_add(xi, yf, r, g, b, a)
	vertices_add(xi, yf, r, g, b, a)
	vertices_add(xf, yi, r, g, b, a)
	vertices_add(xf, yf, r, g, b, a)

def line(**kwargs):
	vertices_set_type('lines')
	xi, yi, xf, yf=_xi_yi(**kwargs)
	r, g, b, a=_color(**kwargs)
	vertices_add(xi, yi, r, g, b, a)
	vertices_add(xf, yf, r, g, b, a)

def clear(**kwargs):
	x, y, w, h=view_get()
	fill(x=x, y=y, w=w, h=h, color=_color(**kwargs))
	vertices_draw()

class VertexBuffer:
	def __init__(self, count):
		self.this=sfml.dans_sfml_wrapper_vertex_buffer_construct(count)

	def __del__(self):
		sfml.dans_sfml_wrapper_vertex_buffer_destruct(self.this)

	def update(self, i, x, y, r, g, b, a):
		sfml.dans_sfml_wrapper_vertex_buffer_update(self.this, i, x, y, r, g, b, a)

	def draw(self):
		sfml.dans_sfml_wrapper_vertex_buffer_draw(self.this)

def capture_start(): sfml.dans_sfml_wrapper_capture_start()
def capture_finish(file_name): sfml.dans_sfml_wrapper_capture_finish(file_name.encode())

def vector_text(s, **kwargs):
	kwargs['xf']=0
	kwargs['w' ]=0
	xi, yi, xf, yf=_xi_yi(**kwargs)
	r, g, b, a=_color(**kwargs)
	vertices_draw()
	sfml.dans_sfml_wrapper_vector_text(xi, yi, yf-yi, s.encode(), r, g, b, a)
	vertices_draw()

class RenderTexture:
	def __init__(self, w, h):
		self._=sfml.dans_sfml_wrapper_render_texture_construct(w, h)

	def __del__(self):
		sfml.dans_sfml_wrapper_render_texture_destruct(self._)

	def draw(self, x, y, w, h):
		if not self.displayed:
			sfml.dans_sfml_wrapper_render_texture_display(self._)
			self.displayed=True
		sfml.dans_sfml_wrapper_render_texture_draw(self._, x, y, w, h)

	def target(self):
		self.displayed=False
		return sfml.dans_sfml_wrapper_render_texture_as_target(self._)

def target_set(targetable): sfml.dans_sfml_wrapper_target_set(targetable.target())
def target_reset(): sfml.dans_sfml_wrapper_target_reset()
