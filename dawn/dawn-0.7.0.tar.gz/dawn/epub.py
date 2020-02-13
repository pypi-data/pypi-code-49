import abc
import collections
import datetime
import lxml.etree
import mimetypes
import posixpath
import uuid
import zipfile

from .utils import E
from .utils import getxmlattr
from .utils import NS


VERSIONS = {}

# this isn't set up correctly in the alpine image ; maybe it should be a package?
mimetypes.add_type('application/pls+xml', '.pls')
mimetypes.add_type('application/smil+xml', '.smil')
mimetypes.add_type('application/x-dtbncx+xml', '.ncx')
mimetypes.add_type('application/xhtml+xml', '.htm')
mimetypes.add_type('application/xhtml+xml', '.html')
mimetypes.add_type('application/xhtml+xml', '.xhtml')
mimetypes.add_type('application/xhtml+xml', '.xml')
mimetypes.add_type('font/otf', '.otf')
mimetypes.add_type('font/ttf', '.ttf')
mimetypes.add_type('font/woff', '.woff')

class Epub(abc.ABC):
	version = None

	_default_toc_path = None

	def __init_subclass__(cls, *args, **kwargs):
		super().__init_subclass__(*args, **kwargs)
		VERSIONS[cls.version] = cls

	def __init__(self, zf, opfpath):
		self._opfpath = opfpath
		self._zf = zf

		self.cover = None
		self.landmarks = Landmarks()
		self.layout = Layout()
		self.manifest = Manifest()
		self.spine = Spine()
		self.toc = Toc(None, None)
		self.meta = {
			'contributors': [], # list of AS with role and file-as
			'creators': [], # list of AS with role and file-as
			'dates': {'creation': None, 'publication': None, 'modification': None},
			'description': None, # AS with lang
			'identifiers': [], # list of AS with id and scheme
			'publisher': None, # AS with lang
			'languages': [],
			'source': None,
			'subjects': [],
			'titles': [], # list of AS with lang
		}

	def _init_read(self, opftree):
		self._read_manifest(opftree)
		self._read_meta(opftree)
		self._read_spine(opftree)
		self._read_toc(opftree)

		uid_id = opftree.get('unique-identifier')
		self.uid = next(filter(lambda i: i.get('id') == uid_id, self.meta['identifiers']), None)

	def _init_write(self):
		self.uid = AttributedString(str(uuid.uuid4()))
		self.uid['id'] = 'uid_id'
		self.uid['scheme'] = 'uuid'
		self.meta['identifiers'] = [self.uid]
		self.meta['languages'] = [AttributedString('und')]

		self.toc.item = self.manifest.add(self._default_toc_path)

		self._writestr('mimetype', b'application/epub+zip', compress_type=zipfile.ZIP_STORED)

		container = E['container'].container(
			{'version': '1.0'},
			E['container'].rootfiles(
				E['container'].rootfile({
					'full-path': self._opfpath,
					'media-type': 'application/oebps-package+xml',
				}),
			),
		)
		self._writestr(
			'META-INF/container.xml',
			lxml.etree.tostring(container, pretty_print=True),
			compress_type=zipfile.ZIP_STORED,
		)

	def _write_opf(self):
		self.meta['dates']['modification'] = datetime.datetime.now()

		if self.toc:
			self._write_toc()

		pkg = self._xml_opf()
		self._writestr(self._opfpath, lxml.etree.tostring(pkg, pretty_print=True))

	@abc.abstractmethod
	def _read_toc(self, opftree): # pragma: no cover
		...

	def _append_to_toc(self, toc, href, title, children):
		# href is relative to self.toc.item
		href = self._from_toc_href(href)
		toc_item = toc.append(href, title)
		for href, title, c in children:
			self._append_to_toc(toc_item.children, href, title, c)

	@abc.abstractmethod
	def _read_meta(self, opftree): # pragma: no cover
		...

	def _read_manifest(self, opftree):
		for item in opftree.findall('./opf:manifest/opf:item', NS):
			self.manifest[getxmlattr(item, 'id')] = getxmlattr(item, 'href')

	def _read_spine(self, opftree):
		for item in opftree.findall('./opf:spine/opf:itemref', NS):
			item = self.manifest[getxmlattr(item, 'idref')]
			self.spine.append(item)

	@abc.abstractmethod
	def _write_toc(self): # pragma: no cover
		...

	def _from_toc_href(self, href):
		root = posixpath.dirname(self.toc.item.href)
		opfdir = posixpath.dirname(self._opfpath)

		href = posixpath.join(opfdir, root, href)
		href = posixpath.relpath(href, opfdir)
		href = posixpath.normpath(href)

		return href

	def _to_toc_href(self, href):
		# href is relative to the opfdir
		# return an href suitable for use in the toc

		opfdir = posixpath.dirname(self._opfpath)
		tocdir = posixpath.dirname(posixpath.join(opfdir, self.toc.item.href))

		href = posixpath.join(opfdir, href)
		href = posixpath.relpath(href, tocdir)
		href = posixpath.normpath(href)

		return href

	def _xml_meta(self):
		return E['opf'].metadata(E['dc'].format('application/epub+zip'))

	def _xml_manifest_item(self, item):
		return E['opf'].item({
			'id': item.iid,
			'href': item.href,
			'media-type': item.mimetype or 'application/octet-stream',
		})

	def _xml_manifest(self):
		return E['opf'].manifest(*(
			self._xml_manifest_item(item)
			for item in sorted(self.manifest.values(), key=lambda it: it.iid)
		))

	def _xml_spine_item(self, item):
		return E['opf'].itemref({'idref': item.iid})

	def _xml_spine(self):
		return E['opf'].spine(*(self._xml_spine_item(item) for item in self.spine))

	def _xml_opf(self):
		return E['opf'].package(
			{'version': self.version, 'unique-identifier': self.uid['id']},
			self._xml_meta(),
			self._xml_manifest(),
			self._xml_spine(),
		)

	def write(self, *args, **kwargs):
		raise NotImplementedError('Use writestr')

	def _writestr(self, *args, **kwargs):
		self._zf.writestr(*args, **kwargs)

	def writestr(self, item, data, **kwargs):
		if isinstance(item, zipfile.ZipInfo):
			raise NotImplementedError('item should be a path relative to the opfdir or an Item')
		if not isinstance(item, self.manifest.Item) or item.iid not in self.manifest:
			item = self.manifest.add(item)

		self._writestr(self.__opfpath(item.href), data, **kwargs)
		return item

	def open(self, item, *args, **kwargs):
		if isinstance(item, self.manifest.Item):
			item = item.href
		return self._zf.open(self.__opfpath(item), *args, **kwargs)

	@property
	def isbn(self):
		for i in self.meta['identifiers']:
			scheme = i.get('scheme', '').lower()
			val = str(i)
			if scheme == 'isbn':
				return i
			if scheme == '' and len(val) == 13 and val[:3] in ('978', '979'):
				return i
		raise KeyError('Unknown ISBN')

	def __opfpath(self, path):
		return posixpath.join(posixpath.dirname(self._opfpath), path)

	def __repr__(self):
		return '<Epub {} (len(manifest): {}, len(spine): {})>'.format(self.version, len(self.manifest), len(self.spine))


class Manifest(dict):
	class Item:
		def __init__(self, iid, href):
			self.iid = iid
			self.href = href

		@property
		def mimetype(self):
			return mimetypes.guess_type(self.href)[0]

		def __repr__(self):
			return '<Manifest.Item {}>'.format(self.__dict__)

	def add(self, item):
		if not isinstance(item, self.Item):
			item = self.Item('item-{}'.format(len(self)), item)
		self[item.iid] = item
		return item

	def __setitem__(self, k, v):
		if isinstance(v, str):
			v = self.Item(k, v)
		if not isinstance(v, self.Item):
			raise TypeError('The manifest needs to be a dict of Manifest.Item')
		super().__setitem__(k, v)

	def byhref(self, href):
		href = href.split('#', 1)[0]
		it = filter(lambda item: item.href == href, self.values())
		try: return next(it)
		except StopIteration: raise KeyError(href)


class Spine(list):
	def append(self, item):
		if not isinstance(item, Manifest.Item):
			raise TypeError('The spine needs to be a list of Manifest.Item')
		return super().append(item)


class TocItems(list):
	class Item:
		def __init__(self, href, title):
			self.href = href # href is the canonical href, relative to the OPF dir
			self.title = title
			self.children = TocItems()

		def __repr__(self):
			return '<Toc.Item {}>'.format(self.__dict__)

	def append(self, item, title=None, children=None):
		if isinstance(item, str):
			if title is None:
				raise TypeError('Need a title to add an href to the TOC')
			item = self.Item(item, title)
			for a in children or []:
				item.children.append(*a)
		if not isinstance(item, self.Item):
			raise TypeError('The TOC needs to be a list of Toc.Item')
		super().append(item)
		return item


class Toc(TocItems):
	def __init__(self, item, title):
		self.item = item
		self.title = title
		super().__init__()


class AttributedString(collections.UserDict):
	def __init__(self, value, **kwargs):
		self.value = value
		self.data = kwargs

	def __bool__(self):
		return bool(self.value)

	def __str__(self):
		return self.value

	def __repr__(self):
		return '<AttributedString {!r} {}>'.format(self.value, self.data)


class Landmarks(list):
	class Item:
		def __init__(self, *, kind, href, title):
			self.kind = kind
			self.href = href
			self.title = title

		def __repr__(self):
			return '<Landmarks.Item {}>'.format(self.__dict__)

	def append(self, item=None, **kwargs):
		if item is None:
			item = self.Item(**kwargs)
		if not isinstance(item, self.Item):
			raise TypeError('The landmarks needs to be a list of Landmarks.Item')
		super().append(item)
		return item


class Layout(dict):
	class Item:
		pass

	class Fixed(Item):
		def __init__(self, *, orientation: str = 'auto', spread: str = 'auto', page_spread: str = None):
			self.orientation = orientation
			self.spread = spread
			self.page_spread = page_spread

		def _copy(self):
			return type(self)(orientation=self.orientation, spread=self.spread, page_spread=self.page_spread)

		def __repr__(self):
			return '<Layout.Fixed {}>'.format(self.__dict__)

	class Reflowable(Item):
		def _copy(self):
			return type(self)()

		def __repr__(self):
			return '<Layout.Reflowable>'

	def __init__(self):
		self.default = self.Reflowable()
		super().__init__()

	def __getitem__(self, key):
		if key not in self:
			self[key] = self.default._copy()
		return super().__getitem__(key)

	def __setitem__(self, key, val):
		if not isinstance(val, self.Item):
			raise TypeError('The layout items needs to be Layout.Item elements')
		super().__setitem__(key, val)
