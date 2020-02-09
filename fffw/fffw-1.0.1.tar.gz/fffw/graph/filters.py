from typing import Optional, Tuple, Any

from fffw.graph import base
from fffw.graph.base import VIDEO, AUDIO

__all__ = [
    'Pass',
    'AudioPass',
    'Deint',
    'Scale',
    'SetSAR',
    'Crop',
    'Split',
    'Concat',
    'AudioConcat',
    'Trim',
    'AudioTrim',
    'SetPTS',
    'AudioSetPTS',
    'AudioSplit',
    'Overlay',
    'Volume',
    'Rotate',
    'Drawtext',
    'HWUpload',
    'ScaleNPP',
]


class Pass(base.Node):
    kind = VIDEO
    enabled = False


class AudioPass(base.Node):
    kind = AUDIO
    enabled = False


class Deint(base.Node):
    kind = VIDEO
    name = 'yadif'

    def __init__(self, mode: str = '0', enabled: bool = True):
        super(Deint, self).__init__(enabled=enabled)
        self.mode = mode

    @property
    def args(self) -> str:
        return "%s" % self.mode


class Scale(base.Node):
    kind = VIDEO
    name = "scale"

    def __init__(self, width: int, height: int, enabled: bool = True):
        super(Scale, self).__init__(enabled=enabled)
        self.width = int(width)
        self.height = int(height)

    @property
    def args(self) -> str:
        return "%sx%s" % (self.width, self.height)


class ScaleNPP(Scale):
    name = 'scale_npp'

    @property
    def args(self) -> str:
        return "w=%s:h=%s" % (self.width, self.height)


class SetSAR(base.Node):
    kind = VIDEO
    name = "setsar"

    def __init__(self, sar: float, enabled: bool = True):
        super(SetSAR, self).__init__(enabled=enabled)
        self.sar = sar

    @property
    def args(self) -> str:
        return "%s" % self.sar


class Crop(base.Node):
    kind = VIDEO
    name = "crop"

    def __init__(self, width: int, height: int, left: int, top: int,
                 enabled: bool = True):
        super(Crop, self).__init__(enabled=enabled)
        self.width = width
        self.height = height
        self.left = left
        self.top = top

    @property
    def args(self) -> str:
        return "%s:%s:%s:%s" % (self.width, self.height, self.left, self.top)


class Split(base.Node):
    kind = VIDEO
    name = "split"

    def __init__(self, output_count: int = 2):
        enabled = output_count > 1
        self.output_count = output_count
        super(Split, self).__init__(enabled=enabled)

    @property
    def args(self) -> str:
        if self.output_count == 2:
            return ''
        return '%s' % self.output_count


class AudioSplit(Split):
    kind = AUDIO
    name = "asplit"


class HWUpload(base.Node):
    kind = VIDEO
    name = 'hwupload_cuda'


class Concat(base.Node):
    kind = VIDEO
    name = 'concat'

    def __init__(self, input_count: int = 2):
        enabled = input_count > 1
        self.input_count = input_count
        super(Concat, self).__init__(enabled=enabled)

    @property
    def args(self) -> str:
        if self.input_count == 2:
            return ''
        return 'n=%s' % self.input_count


class AudioConcat(base.Node):
    kind = AUDIO
    name = 'concat'

    def __init__(self, input_count: int = 2):
        enabled = input_count > 1
        self.input_count = input_count
        super(AudioConcat, self).__init__(enabled=enabled)

    @property
    def args(self) -> str:
        return 'v=0:a=1:n=%s' % self.input_count


class Trim(base.Node):
    kind = VIDEO
    name = 'trim'

    def __init__(self,
                 start: Optional[str] = None,
                 end: Optional[str] = None,
                 enabled: bool = True):
        self.start = start
        self.end = end
        super(Trim, self).__init__(enabled=enabled)

    @property
    def args(self) -> str:
        return 'start=%s:end=%s' % (self.start, self.end)


class AudioTrim(Trim):
    kind = AUDIO
    name = 'atrim'


class SetPTS(base.Node):
    kind = VIDEO
    name = 'setpts'

    def __init__(self, mode: str = 'PTS-STARTPTS', enabled: bool = True):
        self.mode = mode
        super(SetPTS, self).__init__(enabled=enabled)

    @property
    def args(self) -> str:
        return self.mode


class AudioSetPTS(SetPTS):
    kind = AUDIO
    name = 'asetpts'


class Overlay(base.Node):
    kind = VIDEO
    input_count = 2
    name = "overlay"

    def __init__(self, left: int, top: int, enabled: bool = True):
        super(Overlay, self).__init__(enabled=enabled)
        self.left = int(left)
        self.top = int(top)

    @property
    def args(self) -> str:
        return "x=%s:y=%s" % (self.left, self.top)


class Volume(base.Node):
    kind = AUDIO
    name = 'volume'

    def __init__(self, volume: float, enabled: bool = True):
        super(Volume, self).__init__(enabled=enabled)
        self.volume = volume

    @property
    def args(self) -> str:
        return "%.2f" % self.volume


class Rotate(base.Node):
    kind = VIDEO
    name = "rotate"

    def __init__(self, degrees: int, output_size: Tuple[int, int],
                 enabled: bool = True):
        super(Rotate, self).__init__(enabled=enabled)
        self.degrees = degrees
        self.output_size = output_size

    @property
    def args(self) -> str:
        if self.degrees is not None:
            result = "%s*PI/180" % self.degrees
            if self.output_size:
                w, h = self.output_size
                result += ':ow=%s:oh=%s' % (w, h)
            return result
        else:
            raise ValueError(self.degrees)


class Drawtext(base.Node):
    kind = VIDEO
    name = 'drawtext'

    def __init__(self,
                 text: str,
                 fontfile: str = 'font.ttf',
                 x: str = '(w-text_w)/2',
                 y: str = '(h-text_h)/2',
                 enabled: bool = True,
                 **opts: Any):
        super(Drawtext, self).__init__(enabled=enabled)
        self.opts = dict(opts, fontfile=fontfile, text=text, x=x, y=y)

    @property
    def args(self) -> str:
        return ':'.join('%s=%s' % t for t in sorted(self.opts.items()))
