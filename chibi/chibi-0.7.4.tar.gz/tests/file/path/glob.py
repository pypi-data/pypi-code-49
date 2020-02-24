import os
import random
from unittest import TestCase
from unittest.mock import patch

from faker import Factory as Faker_factory

from chibi.file import Chibi_file
from chibi.file.path import Chibi_path
from chibi.file.snippets import exists, ls, file_dir
from tests.snippet.files import Test_with_files


faker = Faker_factory.create()


class Test_glob( Test_with_files ):
    def test_ls_should_return_the_path( self ):
        all_tmps = self.root_dir + 'tmp*'
        ls = all_tmps.ls()
        for l in ls:
            self.assertNotIn( '*', l )

    def test_expand_should_have_all_files( self ):
        source = Chibi_path( self.folder_with_files_with_content ) + '*'
        result = set( source.expand )
        self.assertEqual(
            result, set( self.folder_with_files_with_content.ls() ) )

    def test_ls_with_glob_on_start_should_have_all_items( self ):
        source = Chibi_path( self.folder_with_files_with_content ) + '*'
        result = set( source.ls() )
        self.assertEqual(
            result, set( self.folder_with_files_with_content.ls() ) )

    def test_copy( self ):
        dest = Chibi_path( self.root_dir ) + 'hola'
        self.assertFalse( exists( dest ) )
        source = Chibi_path( self.folder_with_files_with_content ) + '*'
        source.copy( dest )
        self.assertEqual(
            set( f.base_name for f in source.ls() ),
            set( f.base_name for f in dest.ls() ) )
