import os
from itertools import cycle

from musicscore.musictree.treescoretimewise import TreeScoreTimewise

from musurgia.agrandom import AGRandom
from musurgia.agunittest import AGTestCase
from musurgia.arithmeticprogression import ArithmeticProgression
from musurgia.chordfield.chordfield import ChordFieldGroup, ChordField, Breathe
from musurgia.interpolation import InterpolationGroup, RandomInterpolation

path = str(os.path.abspath(__file__).split('.')[0])


class Test(AGTestCase):
    def setUp(self) -> None:
        self.score = TreeScoreTimewise()

    def test_1(self):
        cf_1 = ChordField(quarter_duration=3, midi_generator=cycle([60, 61, 64, 66]))
        cf_2 = ChordField(quarter_duration=6, midi_generator=cycle([72, 73, 74, 73, 72]))
        cfg = ChordFieldGroup()
        cfg.add_field(cf_1)
        cfg.add_field(cf_2)
        xml_path = path + 'test_1.xml'
        cfg.simple_format.to_stream_voice().add_to_score(self.score)
        self.score.write(xml_path)
        self.assertCompareFiles(xml_path)

    def test_2(self):
        cf_1 = ChordField(quarter_duration=3, midi_generator=cycle([60, 61, 64, 66]))
        cf_2 = ChordField(quarter_duration=6, midi_generator=cycle([72, 73, 74, 73, 72]))
        cfg = ChordFieldGroup(duration_generator=AGRandom(pool=[0.2, 0.4, 0.8, 1.6], seed=10))
        cfg.add_field(cf_1)
        cfg.add_field(cf_2)
        xml_path = path + 'test_2.xml'
        cfg.simple_format.to_stream_voice().add_to_score(self.score)
        self.score.write(xml_path)
        self.assertCompareFiles(xml_path)

    def test_3(self):
        cf_1 = ChordField(quarter_duration=3, midi_generator=cycle([60, 61, 64, 66]), duration_generator=cycle([1]))
        cf_2 = ChordField(quarter_duration=6, midi_generator=cycle([72, 73, 74, 73, 72]))
        cfg = ChordFieldGroup(duration_generator=AGRandom(pool=[0.2, 0.4, 0.8, 1.6], seed=10))
        cfg.add_field(cf_1)
        cfg.add_field(cf_2)
        xml_path = path + 'test_3.xml'
        cfg.simple_format.to_stream_voice().add_to_score(self.score)
        self.score.write(xml_path)
        self.assertCompareFiles(xml_path)

    def test_4(self):
        cf_1 = ChordField(quarter_duration=3, midi_generator=cycle([60, 61, 64, 66]), long_ending_mode='post')
        cf_2 = ChordField(quarter_duration=6, midi_generator=cycle([72, 73, 74, 73, 72]))
        cfg = ChordFieldGroup(duration_generator=ArithmeticProgression(a1=0.3, an=1.5))
        cfg.add_field(cf_1)
        cfg.add_field(cf_2)
        xml_path = path + 'test_4.xml'
        cfg.simple_format.to_stream_voice().add_to_score(self.score)
        self.score.write(xml_path)
        self.assertCompareFiles(xml_path)

    def test_5(self):
        times = [3, 7, 3, 10, 3]
        cf_1 = ChordField(quarter_duration=times[0], midi_generator=cycle([72, 73, 74, 73, 72]))
        cf_2 = ChordField(quarter_duration=times[1], midi_generator=cycle([72, 73, 74, 73, 72]))
        cf_3 = ChordField(quarter_duration=times[2], midi_generator=cycle([72, 73, 74, 73, 72]))
        cf_4 = ChordField(quarter_duration=times[3], midi_generator=cycle([72, 73, 74, 73, 72]))
        cf_5 = ChordField(quarter_duration=times[4], midi_generator=cycle([72, 73, 74, 73, 72]))
        points = [1.5, 0.2, 1.5]
        cf_1.duration_generator = ArithmeticProgression(a1=points[0], an=points[0], correct_s=True)
        cf_2.duration_generator = ArithmeticProgression(a1=points[0], an=points[1], correct_s=True)
        cf_3.duration_generator = ArithmeticProgression(a1=points[1], an=points[1], correct_s=True)
        cf_4.duration_generator = ArithmeticProgression(a1=points[1], an=points[0], correct_s=True)
        cf_5.duration_generator = ArithmeticProgression(a1=points[0], an=points[0], correct_s=True)
        cfg = ChordFieldGroup()
        cfg.add_field(cf_1)
        cfg.add_field(cf_2)
        cfg.add_field(cf_3)
        cfg.add_field(cf_4)
        cfg.add_field(cf_5)
        xml_path = path + 'test_5.xml'
        self.score.set_time_signatures(durations=times)
        cfg.simple_format.to_stream_voice().add_to_score(self.score)

        self.score.max_division = 5
        self.score.write(xml_path)
        self.assertCompareFiles(xml_path)

    def test_6(self):
        breathing_durations = [3, 7, 3, 10, 3]
        breathing_break_points = [1.5, 0.2, 1.5]
        breathing = Breathe(quarter_durations=breathing_durations, breakpoints=breathing_break_points)
        midi_generator = InterpolationGroup()
        midi_generator.add_interpolation(
            RandomInterpolation(start=[60, 62, 66, 68], end=[67, 69, 73, 75], duration=13, seed=10))
        midi_generator.add_interpolation(
            RandomInterpolation(start=[67, 69, 73, 75], end=[60, 62, 66, 68], duration=13, seed=11))

        breathing.midi_generator = midi_generator
        xml_path = path + 'test_6.xml'
        self.score.set_time_signatures(durations=breathing_durations)
        breathing.simple_format.to_stream_voice().add_to_score(self.score)

        self.score.max_division = 5
        self.score.write(xml_path)
        self.assertCompareFiles(xml_path)
