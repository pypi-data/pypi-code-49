from functools import partial
from bob.bio.video.annotator import Wrapper
from bob.bio.face.annotator.bobipfacedetect import BobIpFacedetect
from bob.bio.face.annotator.bobipflandmark import BobIpFlandmark
from bob.bio.face.annotator.bobipmtcnn import BobIpMTCNN
from bob.bio.face.annotator.bobipdlib import BobIpDlib
from bob.bio.face.annotator import min_face_size_validator
from bob.bio.base.annotator import FailSafe


def load_frames(biofile, directory, extension):
    return [f for f in biofile.frames]


annotator = Wrapper(
    FailSafe([BobIpMTCNN(), BobIpDlib(), BobIpFacedetect(), BobIpFlandmark()],
             ['leye', 'reye'], only_required_keys=True),
    normalize=True,
    validator=partial(min_face_size_validator, min_face_size=(256, 256)),
    max_age=5,
    read_original_data=load_frames)
