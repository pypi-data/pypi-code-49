from unittest import TestCase
import os

from diff_pdf_visually import pdfdiff


class TestCompareFiles(TestCase):
    """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _compare_pdfs(self, file_path, template_path, verbosity):
        self.assertTrue(pdfdiff(file_path, template_path, verbosity=verbosity))

    def _compare_contents(self, file_path, template_path):
        with open(file_path, 'r') as myfile:
            result = myfile.read()

        with open(template_path, 'r') as myfile:
            template = myfile.read()

        self.assertEqual(template, result)

    def assertExpected(self, file_path, template_path=None, verbosity=0):
        file_name, extension = os.path.splitext(file_path)
        if not template_path:
            if not extension:
                raise ValueError('file_path has no file extension')
            template_path = file_name + '_template' + extension

        if extension == '.pdf':
            self._compare_pdfs(file_path, template_path, verbosity=verbosity)
        else:
            self._compare_contents(file_path, template_path)
