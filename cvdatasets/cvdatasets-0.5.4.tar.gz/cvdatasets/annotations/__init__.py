from cvdatasets.annotations.impl.cub import CUB_Annotations
from cvdatasets.annotations.impl.nab import NAB_Annotations
from cvdatasets.annotations.impl.cars import CARS_Annotations
from cvdatasets.annotations.impl.inat import INAT19_Annotations
from cvdatasets.annotations.impl.flowers import FLOWERS_Annotations
from cvdatasets.annotations.impl.dogs import DOGS_Annotations
from cvdatasets.annotations.impl.hed import HED_Annotations
from cvdatasets.annotations.impl.tigers import TIGERS_Annotations

from cvdatasets.annotations.base import BaseAnnotations
from cvdatasets.annotations.base.bbox_mixin import BBoxMixin
from cvdatasets.annotations.base.parts_mixin import PartsMixin

from cvargparse.utils import BaseChoiceType
from functools import partial

class AnnotationType(BaseChoiceType):
	CUB200 = CUB_Annotations
	CUB200_2FOLD = partial(CUB_Annotations)
	CUB200_GOOGLE = partial(CUB_Annotations)
	CUB200_GOOGLE_SEM = partial(CUB_Annotations)
	NAB = NAB_Annotations
	CARS = CARS_Annotations
	DOGS = DOGS_Annotations
	FLOWERS = FLOWERS_Annotations
	HED = HED_Annotations
	TIGERS = TIGERS_Annotations
	TIGERS_TEST = partial(TIGERS_Annotations)

	INAT19 = INAT19_Annotations
	INAT19_MINI = partial(INAT19_Annotations)
	INAT19_TEST = partial(INAT19_Annotations)

	Default = CUB200
