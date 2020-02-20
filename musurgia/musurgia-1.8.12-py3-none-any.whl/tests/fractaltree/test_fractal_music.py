import os
from unittest import TestCase

from musicscore.musictree.treescoretimewise import TreeScoreTimewise

from musurgia.fractaltree.fractalmusic import FractalMusic
from musurgia.agunittest import AGTestCase

path = os.path.abspath(__file__).split('.')[0]


class Test(TestCase):

    def test_1(self):
        fm = FractalMusic(quarter_duration=12, tree_permutation_order=(3, 1, 2), proportions=[1, 2, 3], multi=(1, 1))
        fm.midi_generator.set_directions(1, 1, -1)
        fm.midi_generator.midi_range = [55, 72]

        fm.add_layer()

        fm.add_layer(lambda n: True if n.fractal_order > 1 else False)
        fm.add_layer(lambda n: True if n.fractal_order > 1 else False)
        fm.add_layer(lambda n: True if n.fractal_order > 1 else False)
        # for node in fm.traverse():
        #     node.chord.add_words(node.midi_generator.midi_range)
        fm.add_layer(lambda n: True if n.fractal_order > 1 else False)

        # for node in fm.traverse():
        #     node.chord.add_words(node.children_generated_midis)
        #     node.chord.add_words(node.midi_generator.directions, relative_y=30)
        #     node.chord.add_words(node.children_generated_midis)
        #     node.chord.add_words(node.permutation_order, relative_y=60)

        score = TreeScoreTimewise()
        score = fm.get_score(score, show_fractal_orders=False)

        xml_path = path + '_test_1.xml'
        score.write(path=xml_path)
        text_path = path + '_test_1.txt'
        fm.write_infos(text_path)
        AGTestCase().assertCompareFiles(actual_file_path=text_path)
        AGTestCase().assertCompareFiles(actual_file_path=xml_path)

    def test_2(self):
        fm = FractalMusic(quarter_duration=12, tree_permutation_order=(3, 1, 2), proportions=[1, 2, 3], multi=(1, 2))
        fm.midi_generator.midi_range = [55, 72]
        fm.add_layer()
        fm.add_layer(lambda n: True if n.fractal_order > 1 else False)
        fm.add_layer(lambda n: True if n.fractal_order > 1 else False)
        fm.add_layer(lambda n: True if n.fractal_order > 1 else False)
        fm.add_layer(lambda n: True if n.fractal_order > 1 else False)

        text_path = path + '_test_2.txt'
        fm.write_infos(text_path)
        AGTestCase().assertCompareFiles(actual_file_path=text_path)
