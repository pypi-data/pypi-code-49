import lxml.etree
import posixpath
import zipfile

from .epub import VERSIONS
from .utils import NS


def _opf_from_metainf(zf):
	try:
		zi = zf.getinfo('META-INF/container.xml')
	except KeyError:
		return

	with zf.open(zi) as f:
		tree = lxml.etree.parse(f)
	rootfile = tree.find('./container:rootfiles/container:rootfile', NS)
	if rootfile is None:
		return

	path = rootfile.get('full-path')
	try:
		return zf.getinfo(path)
	except KeyError:
		return

def _find_opf_zi(zf):
	# adapted from https://github.com/kovidgoyal/calibre/blob/68febe94ca2baf2a0979668b7b61a1e3b0432f0f/src/calibre/ebooks/conversion/plugins/epub_input.py#L233
	# the opf path should be specified in the META-INF/container.xml file, but we try to handle gracefully broken epubs
	zi = _opf_from_metainf(zf)
	if zi is not None:
		return zi

	for zi in zf.infolist():
		if all((
			zi.filename.lower().endswith('.opf'),
			'__MACOSX' not in zi.filename,
			not posixpath.basename(zi.filename).startswith('.'),
		)):
			return zi

	raise ValueError('Not a valid ePub file: could not find the OPF file')

class open:
	def __init__(self, infile, mode='r', version=None, opfpath=None):
		if mode not in ('r', 'w'):
			raise TypeError('Supported modes are r and w')
		if mode == 'r' and opfpath is not None:
			raise TypeError('opfpath should only be used in w mode')
		if mode == 'w' and version is None:
			raise TypeError('version is required in w mode')

		self._mode = mode
		self._opfpath = opfpath
		self._version = version
		self._zf = zipfile.ZipFile(infile, mode=mode)


	def __enter__(self):
		self._zf.__enter__()

		if self._mode == 'r':
			opfzi = _find_opf_zi(self._zf)
			with self._zf.open(opfzi) as f:
				opftree = lxml.etree.parse(f).getroot()

			version = self._version or opftree.get('version')

			self._epub = VERSIONS[version](self._zf, opfzi.filename)
			self._epub._init_read(opftree)

		else:
			assert self._mode == 'w'
			opfpath = self._opfpath or 'content.opf'
			self._epub = VERSIONS[self._version](self._zf, opfpath)
			self._epub._init_write()

		return self._epub

	def __exit__(self, *args):
		if self._mode == 'w':
			self._epub._write_opf()
		self._zf.__exit__(*args)
		del self._epub
		del self._zf
