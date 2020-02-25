import os

from musicscore.musictree.treescoretimewise import TreeScoreTimewise

from musurgia.agunittest import AGTestCase
from musurgia.arithmeticprogression import ArithmeticProgression
from musurgia.chordfield.chordfield import ChordField
from musurgia.fractaltree.fractalmusic import FractalMusic
from musurgia.interpolation import Interpolation

path = str(os.path.abspath(__file__).split('.')[0])


class Test(AGTestCase):
    def setUp(self) -> None:
        self.score = TreeScoreTimewise()

    def test_1(self):
        fm = FractalMusic(quarter_duration=20, tempo=80)
        fm.midi_generator.midi_range = [60, 84]
        fm.add_layer()
        sorted_children = sorted(fm.get_children(), key=lambda child: child.fractal_order)
        sorted_children[-1].chord_field = ChordField(duration_generator=ArithmeticProgression(a1=0.2, an=2),
                                                     midi_generator=Interpolation(start=84, end=60, duration=None,
                                                                                  key=lambda midi: round(midi * 2) / 2))

        score = fm.get_score(show_fractal_orders=True)
        xml_path = path + '_test_1.xml'
        score.write(xml_path)
        self.assertCompareFiles(xml_path)

    def test_2(self):
        def add_chord_field(child):
            child.chord_field = ChordField(duration_generator=ArithmeticProgression(a1=0.2, an=2),
                                           midi_generator=Interpolation(start=child.midi_generator.midi_range[0],
                                                                        end=child.midi_generator.midi_range[1],
                                                                        duration=None,
                                                                        key=lambda
                                                                            midi: round(midi * 2) / 2),
                                           short_ending_mode='prolong')

        fm = FractalMusic(quarter_duration=20, tempo=80, proportions=[1, 2, 3, 4, 5],
                          tree_permutation_order=[3, 1, 5, 2, 4])
        fm.midi_generator.midi_range = [60, 84]
        fm.add_layer()
        sorted_children = sorted(fm.get_children(), key=lambda child: child.fractal_order)
        add_chord_field(sorted_children[-1])

        score = fm.get_score(show_fractal_orders=True)
        xml_path = path + '_test_2.xml'
        score.write(xml_path)
