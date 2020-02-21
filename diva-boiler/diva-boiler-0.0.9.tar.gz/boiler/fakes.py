from typing import List

from factory import Factory, Faker, lazy_attribute, SubFactory

from boiler import definitions, models

MAX_FRAME = 30 * 60 * 5


class BoxFactory(Factory):
    class Meta:
        model = models.Box

    left: int = Faker('random_int', min=0, max=1070)
    top: int = Faker('random_int', min=0, max=750)

    @lazy_attribute
    def right(self) -> int:
        return Faker('random_int', min=self.left + 10, max=1080).generate()

    @lazy_attribute
    def bottom(self) -> int:
        return Faker('random_int', min=self.top + 10, max=760).generate()


class DetectionFactory(Factory):
    class Meta:
        model = models.Detection

    frame: int = Faker('random_int', min=0, max=MAX_FRAME)
    box: models.Box = SubFactory(BoxFactory)
    keyframe: bool = Faker('random_element', elements=[True, False])


class ActorFactory(Factory):
    class Meta:
        model = models.Actor

    actor_type: models.ActorType = Faker('random_element', elements=definitions.ActorType)
    begin: int = Faker('random_int', min=0, max=MAX_FRAME - 10)

    @lazy_attribute
    def end(self) -> int:
        return Faker('random_int', min=self.begin + 10, max=MAX_FRAME).generate()

    @lazy_attribute
    def detections(self) -> List[models.Detection]:
        return [
            DetectionFactory(frame=self.begin, keyframe=True),
            DetectionFactory(frame=self.end, keyframe=True),
        ]


class ActivityFactory(Factory):
    class Meta:
        model = models.Activity

    activity_type: definitions.ActivityType = Faker(
        'random_element', elements=definitions.ActivityType
    )
    begin: int = Faker('random_int', min=0, max=MAX_FRAME - 10)

    @lazy_attribute
    def end(self) -> int:
        return Faker('random_int', min=self.begin + 10, max=MAX_FRAME).generate()

    @lazy_attribute
    def actors(self) -> List[models.Actor]:
        return [
            ActorFactory(),
            ActorFactory(),
        ]
