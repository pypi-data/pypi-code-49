import collections

import shapely.geometry, shapely.ops

import esy.osm.pbf


def is_point(entry):
    return type(entry) is esy.osm.pbf.Node


def is_linestring(entry):
    if type(entry) is not esy.osm.pbf.Way: return False
    return entry.tags.get('area', 'no') == 'no'


def is_polygon(entry):
    if type(entry) is not esy.osm.pbf.Way: return False
    if entry.tags.get('area') == 'no': return False
    return entry.refs[0] == entry.refs[-1]


def is_multipolygon(entry):
    if type(entry) is not esy.osm.pbf.Relation: return False
    return entry.tags.get('type') == 'multipolygon'


def merge_touching_rings(rings):
    '''
    Search and merge touching rings.

    OSM polygons deviate from OGC simple features in inner rings of a
    multipolygon. They may touch in OSM but not in OGC.
    '''
    merged = []
    to_merge = list(rings)
    while to_merge:
        a = to_merge.pop(0)
        while True:
            for b in to_merge:
                if a.overlaps(b):
                    a = shapely.ops.unary_union((
                        shapely.geometry.Polygon(a), shapely.geometry.Polygon(b)
                    ))
                    a = shapely.geometry.LinearRing(a.exterior.coords)
                    to_merge.remove(b)
                    break
            else:
                break
        merged.append(a)
    return merged


def merge_segments_to_rings(segments, candidate=None, assigned=None):
    '''
    Iterates all rings that can be merged from segments. Note that rings are not
    necessarily linear.
    '''
    if not candidate:
        candidate, assigned = segments[0], set([0])

    if candidate[0] == candidate[-1]:
        yield candidate, assigned

    for idx, segment in enumerate(segments):
        if idx in assigned:
            continue

        if candidate[-1] == segment[0]:
            yield from merge_segments_to_rings(
                segments, candidate + segment[1:], assigned | set([idx])
            )
        elif candidate[-1] == segment[-1]:
            yield from merge_segments_to_rings(
                segments, candidate + segment[:-1][::-1], assigned | set([idx])
            )


def multipolygon_shape(relation, ways, nodes):
    '''
    Converts an [openstreetmap multipolygon](
    https://wiki.openstreetmap.org/wiki/Relation:multipolygon) to a
    [shapely multipolygon](
    https://shapely.readthedocs.io/en/latest/manual.html#MultiPolygon).
    '''
    geoms = []

    # Collect node references for outer and inner rings.
    rings = dict(outer=[], inner=[])
    for rel_id, role_type, role in relation.members:
        if role_type != 'WAY':
            continue
        if role == '':
            # Assume role is outer.
            role = 'outer'
        rings[role].append(list(ways[rel_id].refs))

    # Merge segments to rings.
    for role, segments in rings.items():
        rings[role] = []
        while segments:
            for candidate, assigned in merge_segments_to_rings(segments):
                ring = shapely.geometry.polygon.LinearRing(
                    [nodes[i].lonlat for i in candidate]
                )
                if ring.is_valid:
                    break
            else:
                raise ValueError('Invalid segments')

            # Prune assigned segments.
            segments = [s for i, s in enumerate(segments) if i not in assigned]

            # Switch winding order.
            if ring.is_ccw != (role == 'outer'):
                ring.coords = ring.coords[::-1]
            assert ring.is_ccw == (role == 'outer')
            rings[role].append(ring)

    for outer in rings['outer']:
        # Construct a polygon from the outer ring to check which inner rings
        # it contains.
        outer = shapely.geometry.Polygon(outer)
        interiors = list(map(outer.contains, rings['inner']))

        holes = [r for r, i in zip(rings['inner'], interiors) if i]

        # Prune inner rings.
        rings['inner'] = [
            r for r, i in zip(rings['inner'], interiors) if not i
        ]

        # Rebuild outer polygon with holes.
        # TODO Is it possible to reuse the original outer polygon?
        shape = shapely.geometry.Polygon(list(outer.exterior.coords), holes)
        if not shape.is_valid:
            # Try to merge touching inner rings (which is an OSM exception).
            holes = merge_touching_rings(holes)
            shape = shapely.geometry.Polygon(list(outer.exterior.coords), holes)
            if not shape.is_valid:
                raise ValueError(
                    'Invalid outer ring in multipolygon relation {}'.format(
                        relation
                    )
                )
        geoms.append(shape)

    shape = shapely.geometry.MultiPolygon(geoms)
    if not shape.is_valid:
        raise ValueError('Invalid multipolygon relation {}'.format(relation))
    shape.id = relation.id
    shape.tags = relation.tags
    return shape


PENDING = object()


class Event(object):
    def __init__(self, context):
        self.context = context
        self.ok = None
        self.value = PENDING
        self.callbacks = []

    def _trigger(self, ok, value):
        if not ok and not self.callbacks and not hasattr(self, 'defused'):
            raise RuntimeError('Unhandled failure') from value
        for callback in self.callbacks:
            self.context.queue.append((callback, ok, value))
        self.ok, self.value, self.callbacks = ok, value, None


class Task(Event):
    def __init__(self, context, generator):
        self.context = context
        self.ok = None
        self.value = PENDING
        self.callbacks = []
        self.generator = generator
        self.context.queue.append((self, True, None))

    def __call__(self, ok, value):
        try:
            while True:
                if ok:
                    event = self.generator.send(value)
                else:
                    event = self.generator.throw(value)

                try:
                    if event.callbacks is not None:
                        event.callbacks.append(self)
                        return
                    ok, value = event, event.value
                except Exception as e:
                    if isinstance(event, Event):
                        raise e
                    ok = False
                    value = RuntimeError('{} is not a Event'.format(event))
        except StopIteration as e:
            self._trigger(True, e.args[0] if e.args else None)
        except RuntimeError as e:
            # RuntimeError are critical errors and their handling cannot be
            # deferred to callbacks.
            raise e
        except Exception as e:
            self._trigger(False, e)


class Context(object):
    current = None

    def __init__(self):
        self.queue = collections.deque()
        self.context = None

    def __enter__(self):
        self.context, Context.current = Context.current, self

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.context, Context.current = None, self.context

    def compute(self, event=None):
        if Context.current is not self:
            raise RuntimeError('Context {} is not active'.format(self))

        if event is None:
            event = Event(self)
            event._trigger(True, None)

        while event.value is PENDING:
            if not self.queue:
                raise RuntimeError('Queue is empty')
            func, *args = self.queue.popleft()
            func(*args)
        return event.value


class Shape(object):
    def __init__(self, osmfile, context=None):
        if type(osmfile) is str:
            osmfile = esy.osm.pbf.File(osmfile)
        self.osmfile = osmfile
        if context is None:
            context = Context()
        self.context = context
        self._todo = None
        self.blockmap = {}
        self.blockref = {}
        self._requests = []
        self._requestmap = {}

    def iter_tasks(self, filter, max_tasks=2 ** 16):
        tasks = []
        for block in self.osmfile.blocks:
            for entry in block:
                if filter(entry):
                    if is_multipolygon(entry):
                        task = Task(self.context, self.multipolygon(entry))
                    elif is_polygon(entry):
                        task = Task(self.context, self.polygon(entry))
                    elif is_linestring(entry):
                        task = Task(self.context, self.linestring(entry))
                    elif is_point(entry):
                        task = Task(self.context, self.point(entry))
                    else:
                        print('Unsupported entry', entry)
                        continue
                    tasks.append(task)

                    if len(tasks) >= max_tasks:
                        yield from tasks
                        tasks = []
        yield from tasks

    def __call__(self, filter, max_tasks=2 ** 16):
        with self.context:
            for task in self.iter_tasks(filter, max_tasks):
                yield self.context.compute(task)

    def entries(self, ids):
        event, entries = Event(self.context), []
        if not self._requests:
            self.context.queue.append((self._handle_requests,))
        self._requests.append((event, entries))
        for id in ids:
            events = self._requestmap.get(id)
            if events is None:
                self._requestmap[id] = events = []
            events.append(entries)
        return event

    def _handle_requests(self):
        for entry in self.osmfile:
            requests = self._requestmap.get(entry.id)
            if requests is None:
                continue
            for entries in requests:
                entries.append(entry)

        for event, result in self._requests:
            event._trigger(True, result)
        self._requests, self._requestmap = [], {}

    def point(self, node):
        shape = shapely.geometry.Point(node.lonlat)
        shape.id = node.id
        shape.tags = node.tags
        return shape
        yield

    def linestring(self, way):
        nodes = {
            entry.id: entry
            for entry in (yield self.entries(way.refs))
            if type(entry) is esy.osm.pbf.Node
        }

        shape = shapely.geometry.LineString([nodes[i].lonlat for i in way.refs])
        shape.id = way.id
        shape.tags = way.tags
        return shape

    def polygon(self, way):
        nodes = {
            entry.id: entry
            for entry in (yield self.entries(way.refs))
            if type(entry) is esy.osm.pbf.Node
        }

        outer = shapely.geometry.polygon.LinearRing(
            [nodes[i].lonlat for i in way.refs]
        )

        # Switch winding order if necessary.
        if not outer.is_ccw:
            outer.coords = outer.coords[::-1]
        shape = shapely.geometry.Polygon(outer)
        if not shape.is_valid:
            raise ValueError('Invalid polygon {}'.format(way.tags))
        shape.id = way.id
        shape.tags = way.tags
        return shape

    def multipolygon(self, relation):
        way_ids = set(
            id for id, type, role in relation.members if type == 'WAY'
        )

        ways = {
            entry.id: entry
            for entry in (yield self.entries(way_ids))
            if type(entry) is esy.osm.pbf.Way
        }

        node_ids = set.union(*(set(w.refs) for w in ways.values()))
        nodes = {
            entry.id: entry
            for entry in (yield self.entries(node_ids))
            if type(entry) is esy.osm.pbf.Node
        }
        return multipolygon_shape(relation, ways, nodes)
