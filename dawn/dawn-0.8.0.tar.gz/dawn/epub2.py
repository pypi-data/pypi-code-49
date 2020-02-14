import itertools
import logging
import lxml.etree

from .epub import AttributedString
from .epub import Epub
from .utils import E
from .utils import getxmlattr
from .utils import ns
from .utils import NS
from .utils import parse_date


logger = logging.getLogger(__name__)

class Epub20(Epub):
	version = '2.0'
	_default_toc_path = 'toc.ncx'

	def _read_toc(self, opftree):
		toc_id = getxmlattr(opftree.find('./opf:spine', NS), 'toc')
		if toc_id is None:
			return

		def parse(tag):
			for np in tag.findall('./ncx:navPoint', NS):
				content = np.find('./ncx:content', NS)
				if content is None:
					continue
				text = np.find('./ncx:navLabel/ncx:text', NS)
				yield (
					getxmlattr(content, 'src'),
					(text.text if text is not None else None) or '',
					parse(np),
				)

		self.toc.item = self.manifest[toc_id]
		with self.open(self.toc.item) as f:
			ncx = lxml.etree.parse(f).getroot()

		for a in parse(ncx.find('./ncx:navMap', NS)):
			self._append_to_toc(self.toc, *a)

		title_tag = ncx.find('./ncx:docTitle/ncx:text', NS)
		if title_tag is not None:
			self.toc.title = title_tag.text or ''

	__meta = [
		# tag, attributes, multiple
		('title', ('xml:lang',), True),
		('creator', ('opf:role', 'opf:file-as'), True),
		('subject', (), True),
		('description', (), False),
		('publisher', (), False),
		('contributor', ('opf:role', 'opf:file-as'), True),
		# Drop type
		# Drop format
		# date handled manually
		('identifier', ('id', 'opf:scheme'), True),
		('source', (), False),
		('language', (), True),
		# Drop relation
		# Drop coverage
		# Drop rights
	]
	def _read_meta(self, opftree):
		metadata = opftree.find('./opf:metadata', NS)
		def extract(tag, attrs, ns='dc'):
			for t in metadata.findall('{}:{}'.format(ns, tag), NS):
				yield AttributedString(t.text or '', **{
					k.split(':', 1)[-1]: getxmlattr(t, k)
					for k in attrs
					if getxmlattr(t, k) is not None
				})

		for tag, attrs, multi in self.__meta:
			f = list if multi else lambda d: next(d, None)
			self.meta[tag + ('s' if multi else '')] = f(extract(tag, attrs))

		for astr in extract('date', ('opf:event',)):
			if 'event' not in astr:
				continue
			if astr['event'] in self.meta['dates']:
				self.meta['dates'][astr['event']] = parse_date(astr)

		for astr in extract('meta', ('name', 'content'), ns='opf'):
			if astr.get('name') == 'cover':
				try:
					cover = self.manifest[astr['content']]
				except KeyError:
					logger.debug('Cover not found: %s', astr['content'])
				else:
					self.cover = cover

		guide = opftree.find('./opf:guide', NS)
		if guide is not None:
			for t in guide.findall('opf:reference', NS):
				self.landmarks.append(
					kind=getxmlattr(t, 'type'),
					title=getxmlattr(t, 'title'),
					href=getxmlattr(t, 'href'),
				)

	def _xml_meta(self):
		for k, li in (('Default', self.layout.default), *self.layout.items()):
			if not isinstance(li, self.layout.Reflowable):
				raise ValueError('ePub 2.0 only support reflowable layouts. Invalid layout {}: {!r}'.format(k, li))

		meta = super()._xml_meta()

		for k, v in self.meta['dates'].items():
			if v is not None:
				meta.append(E['dc'].date(
					v.strftime('%Y-%m-%dT%H:%M:%SZ'),
					{ns('opf:event'): k},
				))

		for tag, attrs, multi in self.__meta:
			todo = self.meta.get(tag + ('s' if multi else ''))
			if not todo:
				continue
			if not multi:
				todo = [todo]
			for astr in todo:
				tag = getattr(E['dc'], tag)(str(astr))
				for k in attrs:
					val = astr.get(k.split(':', 1)[-1])
					if val:
						tag.attrib[ns(k)] = val
				meta.append(tag)

		if self.cover is not None:
			meta.append(E['opf'].meta({'name': 'cover', 'content': self.cover.iid}))

		return meta

	def _xml_spine(self):
		spine = super()._xml_spine()
		if self.toc.item is not None:
			spine.attrib['toc'] = self.toc.item.iid
		return spine

	def _xml_opf(self):
		res = super()._xml_opf()
		if self.landmarks:
			res.append(E['opf'].guide(*(
				E['opf'].reference({'type': it.kind, 'title': it.title, 'href': it.href})
				for it in self.landmarks
			)))
		return res

	def _write_toc(self):
		ids = itertools.count()

		def depth(toc):
			if not toc:
				return 0
			return max(depth(item.children) for item in toc) + 1

		def navpoints(toc):
			for item in toc:
				np = E['ncx'].navPoint(
					{'id': 'np-{}'.format(next(ids))},
					E['ncx'].navLabel(E['ncx'].text(item.title)),
					E['ncx'].content({'src': self._to_toc_href(item.href)}),
				)
				if item.children:
					for c in navpoints(item.children):
						np.append(c)
				yield np

		toc = E['ncx'].ncx(
			{'version': '2005-1'},
			E['ncx'].head(
				E['ncx'].meta({'name': 'dtb:uid', 'content': str(self.uid)}),
				E['ncx'].meta({'name': 'dtb:depth', 'content': str(depth(self.toc))}),
			),
			E['ncx'].docTitle(E['ncx'].text(self.toc.title or '')),
			E['ncx'].navMap(*navpoints(self.toc)),
		)

		data = lxml.etree.tostring(toc, pretty_print=True)
		self.writestr(self.toc.item, data)
