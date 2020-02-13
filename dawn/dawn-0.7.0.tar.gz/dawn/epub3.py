import lxml.etree
import re
import uuid

from .epub import AttributedString
from .epub import Epub
from .utils import E
from .utils import getxmlattr
from .utils import ns
from .utils import NS
from .utils import parse_date


class Epub30(Epub):
	version = '3.0'
	_default_toc_path = 'toc.xhtml'

	def _read_manifest(self, opftree):
		super()._read_manifest(opftree)
		for item in opftree.findall('./opf:manifest/opf:item', NS):
			iid = getxmlattr(item, 'id')
			val = getxmlattr(item, 'properties')
			if val == 'nav':
				self.toc.item = self.manifest[iid]
			if val == 'cover-image':
				self.cover = self.manifest[iid]

	def _read_spine(self, opftree):
		super()._read_spine(opftree)
		for item in opftree.findall('./opf:spine/opf:itemref', NS):
			iid = getxmlattr(item, 'idref')
			val = getxmlattr(item, 'properties')
			if not val:
				continue

			props = set(val.split(' '))
			parsed = {}

			for val in props:
				for prop, attr in (
					('rendition:orientation-', 'orientation'),
					('rendition:spread-', 'spread'),
					('rendition:page-spread-', 'page_spread'),
					('page-spread-', 'page_spread'),
				):
					if val.startswith(prop):
						parsed[attr] = val[len(prop):]

			WantedLayout = type(self.layout.default)
			if 'rendition:layout-reflowable' in props:
				WantedLayout = self.layout.Reflowable
			elif 'rendition:layout-pre-paginated' in props:
				WantedLayout = self.layout.Fixed

			if not parsed and WantedLayout == type(self.layout.default):
				continue

			if isinstance(self.layout.default, WantedLayout):
				self.layout[iid] = self.layout.default._copy()
			else:
				self.layout[iid] = WantedLayout()


			# todo: log a warning if parsed is not empty and WantedLayout is Reflowable
			for k, v in parsed.items():
				setattr(self.layout[iid], k, v)

	def _read_toc(self, opftree):
		if self.toc.item is None:
			return

		with self.open(self.toc.item) as f:
			toc = lxml.etree.parse(f).getroot()

		nav = toc.find('.//html:nav[@ops:type="toc"]', NS)

		def parse(tag):
			if tag is None:
				return
			for li in tag.findall('./html:li', NS):
				a = li.find('./html:a', NS)
				if a is None:
					continue
				nested = li.find('./html:ol', NS)
				href = getxmlattr(a, 'href')
				if href is not None:
					title = a.xpath('string()').strip()
					title = re.sub(r'\s+', ' ', title)
					yield (href, title, parse(nested))

		for a in parse(nav.find('./html:ol', NS)):
			self._append_to_toc(self.toc, *a)

		title_tag = nav.find('.//html:h2', NS)
		if title_tag is not None:
			self.toc.title = title_tag.text or ''


		nav = toc.find('.//html:nav[@ops:type="landmarks"]', NS)
		if nav is not None:
			for li in nav.findall('./html:ol/html:li', NS):
				a = li.find('./html:a', NS)
				self.landmarks.append(
					kind=getxmlattr(a, 'ops:type'),
					href=getxmlattr(a, 'href'),
					title=a.text or '',
				)

	__meta = [
		# tag, attributes, multiple
		('identifier', (), True), # identifier-type is mapped to scheme manually
		('title', (('xml:lang', 'lang'),), True),
		('language', (), True),
		('contributor', (), True),
		# Drop coverage
		('creator', (), True),
		# manually handle dates
		('description', (('xml:lang', 'lang'),), False),
		# Drop format
		('publisher', (('xml:lang', 'lang'),), False),
		# Drop relation
		# Drop rights
		('source', (), False),
		('subject', (), True),
		# Drop type
	]
	__dates = [
		('created', 'creation'),
		('date', 'publication'),
		('modified', 'modification'),
	]
	def _read_meta(self, opftree):
		metadata = opftree.find('./opf:metadata', NS)

		def extract(tag, attrs):
			for t in metadata.findall('dc:' + tag, NS):
				res = AttributedString(t.text or '', **{
					target: getxmlattr(t, key)
					for key, target in attrs
					if getxmlattr(t, key) is not None
				})
				if getxmlattr(t, 'id') is not None:
					res['id'] = getxmlattr(t, 'id')
					for refine in metadata.findall('opf:meta/[@refines="#{}"]'.format(res['id']), NS):
						res[getxmlattr(refine, 'property')] = refine.text or ''
				yield res

		for tag, attrs, multi in self.__meta:
			f = list if multi else lambda it: next(it, None)
			self.meta[tag + ('s' if multi else '')] = f(extract(tag, attrs))

		for identifier in self.meta['identifiers']:
			if 'identifier-type' in identifier:
				identifier['scheme'] = identifier.pop('identifier-type')

		for tag, k in self.__dates:
			date = metadata.find('opf:meta/[@property="dcterms:{}"]'.format(tag), NS)
			if date is not None:
				self.meta['dates'][k] = parse_date(date.text or '')

		tag = metadata.find('opf:meta/[@property="rendition:layout"]', NS)
		if tag is not None:
			if tag.text == 'pre-paginated':
				self.layout.default = self.layout.Fixed()
				tag = metadata.find('opf:meta/[@property="rendition:orientation"]', NS)
				if tag is not None:
					self.layout.default.orientation = tag.text or ''
				tag = metadata.find('opf:meta/[@property="rendition:spread"]', NS)
				if tag is not None:
					self.layout.default.spread = tag.text or ''
			else:
				# todo: warn if not reflowable
				pass # default is reflowable

	def _xml_meta(self):
		meta = super()._xml_meta()

		for tag, k in self.__dates:
			val = self.meta['dates'].get(k)
			if val:
				meta.append(E['opf'].meta(
					{'property': 'dcterms:{}'.format(tag)},
					val.strftime('%Y-%m-%dT%H:%M:%SZ'),
				))

		for tag, attrs, multi in self.__meta:
			todo = self.meta.get(tag + ('s' if multi else ''))
			if not todo:
				continue
			if not multi:
				todo = [todo]
			for astr in todo:
				attrs_to_add = dict(astr)
				m = getattr(E['dc'], tag)(str(astr))
				for k, t in attrs + (('id', 'id'),):
					val = attrs_to_add.pop(t, None)
					if val:
						m.attrib[ns(k)] = val
				meta.append(m)
				if attrs_to_add:
					if 'id' not in m.attrib:
						m.attrib['id'] = str(uuid.uuid4())
					for k, v in attrs_to_add.items():
						if k == 'scheme': k = 'identifier-type'
						meta.append(E['opf'].meta(str(v), {
							'refines': '#{}'.format(m.attrib['id']),
							'property': k,
						}))

		if isinstance(self.layout.default, self.layout.Reflowable):
			meta.append(E['opf'].meta({'property': 'rendition:layout'}, 'reflowable'))
		else:
			meta.append(E['opf'].meta({'property': 'rendition:layout'}, 'pre-paginated'))
			meta.append(E['opf'].meta({'property': 'rendition:orientation'}, self.layout.default.orientation))
			meta.append(E['opf'].meta({'property': 'rendition:spread'}, self.layout.default.spread))

		return meta

	def _xml_manifest_item(self, item):
		res = super()._xml_manifest_item(item)
		if item is self.toc.item:
			res.attrib['properties'] = 'nav'
		if item is self.cover:
			res.attrib['properties'] = 'cover-image'
		return res

	def _xml_spine_item(self, item):
		res = super()._xml_spine_item(item)
		if item.iid in self.layout:
			layout = self.layout[item.iid]
			props = []

			if type(layout) != type(self.layout.default):
				key = {
					self.layout.Reflowable: 'reflowable',
					self.layout.Fixed: 'pre-paginated',
				}[type(layout)]
				props.append('layout-{}'.format(key))

			if isinstance(layout, self.layout.Fixed):
				if not isinstance(self.layout.default, self.layout.Fixed) or layout.orientation != self.layout.default.orientation:
					props.append('orientation-{}'.format(layout.orientation))
				if not isinstance(self.layout.default, self.layout.Fixed) or layout.spread != self.layout.default.spread:
					props.append('spread-{}'.format(layout.spread))
				if layout.page_spread is not None:
					props.append('page-spread-{}'.format(layout.page_spread))

			if props:
				res.attrib['properties'] = ' '.join('rendition:{}'.format(p) for p in props)
		return res

	def _write_toc(self):
		title = self.toc.title or 'Table of contents'

		def ol(toc):
			res = E['html'].ol()
			for item in toc:
				np = E['html'].li(
					E['html'].a(item.title, {'href': self._to_toc_href(item.href)}),
				)
				if item.children:
					np.append(ol(item.children))
				res.append(np)
			return res

		body = E['html'].body(E['html'].nav(
			{ns('ops:type'): 'toc'},
			E['html'].h2(title),
			ol(self.toc),
		))

		if self.landmarks:
			body.append(E['html'].nav(
				{ns('ops:type'): 'landmarks'},
				E['html'].ol(*(
					E['html'].li(
						E['html'].a(it.title, {'href': it.href, ns('ops:type'): it.kind})
					)
					for it in self.landmarks
				)),
			))

		data = E['html'].html(
			E['html'].head(
				E['html'].title(title),
				E['html'].meta({'charset': 'utf-8'}),
			),
			body,
		)

		data = lxml.etree.tostring(data, pretty_print=True, method='html')

		self.writestr(self.toc.item, data)
