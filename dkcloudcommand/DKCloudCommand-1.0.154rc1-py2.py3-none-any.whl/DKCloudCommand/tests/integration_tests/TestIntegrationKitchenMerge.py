import os
import shutil
import time
import unittest

from click.testing import CliRunner

from DKCommon.DKPathUtils import normalize, WIN

from DKCloudCommand.tests.integration_tests.BaseTestCloud import BaseTestCloud
from DKCloudCommand.cli.__main__ import dk
from DKCloudCommand.modules.DKFileHelper import DKFileHelper


class TestIntegrationKitchenMerge(BaseTestCloud):
    """
        Naming convention:
        ---------------------------------------
        NC	        No change
        D	        Delete
        M	        Modifiy
        RNCA	    Rename no change to new name A
        RMA	        Rename and modify to new name A
        RNCB	    Rename no change to new name B
        RMB	        Rename and modify to new name B
    """

    def test_1_nc_nc(self):
        self._init('1_nc_nc')

        # do merge preview
        conflict_list = []
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_content(recipe_dir_target_check, self.conflicted_file)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file_new)

        # cleanup
        self._cleanup()

    def test_2_nc_d(self):
        self._init('2_nc_d')

        self._delete(self.target_kitchen, self.recipe_dir_target, self.conflicted_file)

        # do merge preview
        conflict_list = []
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file_new)

        # cleanup
        self._cleanup()

    def test_3_nc_m(self):
        self._init('3_nc_m')

        self._update(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file, self.target_contents
        )

        # do merge preview
        conflict_list = []
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file, content=self.target_contents
        )
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file_new)

        # cleanup
        self._cleanup()

    def test_4_nc_rnca(self):
        self._init('4_nc_rnca')

        self._rename(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file,
            self.conflicted_file_new
        )

        # do merge preview
        conflict_list = []
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(recipe_dir_target_check, self.conflicted_file_new)

        # cleanup
        self._cleanup()

    def test_5_nc_rma(self):
        self._init('5_nc_rma')

        self._rename(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file,
            self.conflicted_file_new, self.target_contents
        )

        # do merge preview
        conflict_list = []
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new, content=self.target_contents
        )

        # cleanup
        self._cleanup()

    def test_8_d_nc(self):
        self._init('8_d_nc')

        self._delete(self.source_kitchen, self.recipe_dir_source, self.conflicted_file)

        # do merge preview
        conflict_list = [
            ['ok', self.conflicted_file],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file_new)

        # cleanup
        self._cleanup()

    def test_12_d_rma(self):
        self._init('12_d_rma')

        self._delete(self.source_kitchen, self.recipe_dir_source, self.conflicted_file)
        self._rename(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file,
            self.conflicted_file_new, self.target_contents
        )

        # do merge preview
        warnings = [
            "File '%s/%s': renamed or deleted in source kitchen; renamed or deleted in target kitchen"
            % (self.recipe, self.conflicted_file)
        ]

        conflict_list = [
            ['ok', self.conflicted_file],
        ]
        self._merge_preview(
            resolved=False, conflict_list=conflict_list, cpr=True, warnings=warnings
        )

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new, content=self.target_contents
        )

        # cleanup
        self._cleanup()

    def test_15_m_nc(self):
        self._init('15_m_nc')

        # change file1 in source file
        self._update(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file, self.source_contents
        )

        # change file2 in source file
        self._update(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file_new,
            self.source_contents2
        )

        # do merge preview before resolving conflicts
        conflict_list = [
            ['ok', self.conflicted_file_new],
            ['ok', self.conflicted_file],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file, content=self.source_contents
        )
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new, content=self.source_contents2
        )

        # cleanup
        self._cleanup()

    def test_54_m_nc_fast_forward_reverse(self):
        self._init('54_m_nc_fast_forward_reverse')

        # change file1 in source file
        self._update(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file, self.source_contents
        )

        # change file2 in source file
        self._update(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file_new,
            self.source_contents2
        )

        # do merge preview before resolving conflicts
        conflict_list = [
            ['ok', self.conflicted_file_new],
            ['ok', self.conflicted_file],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # do merge
        self._merge(conflict_list=conflict_list)

        # reverse merge
        conflict_list = []
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True, reverse=True)
        self._merge(conflict_list=conflict_list, reverse=True)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file, content=self.source_contents
        )
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new, content=self.source_contents2
        )

        # cleanup
        self._cleanup()

    def test_17_m_m(self):
        self._init('17_m_m')

        # changes
        self._update(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file, self.source_contents
        )
        self._update(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file, self.target_contents
        )

        # do merge preview before resolving conflicts
        conflict_list = [
            ['conflict', self.conflicted_file],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # Resolve the conflict
        self._resolve_conflict(self.conflicted_file, self.merge_contents)

        # do merge preview after resolving conflicts
        self._merge_preview(resolved=True, conflict_list=conflict_list, cpr=False)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file, content=self.merge_contents
        )
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file_new)

        # cleanup
        self._cleanup()

    def test_18_m_rnca(self):
        self._init('18_m_rnca')

        self._update(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file, self.source_contents
        )
        self._rename(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file,
            self.conflicted_file_new
        )

        # do merge preview before resolving conflicts
        warnings = [
            "File '%s/%s': modified in source kitchen; renamed to '%s/%s' in target kitchen" %
            (self.recipe, self.conflicted_file, self.recipe, self.conflicted_file_new)
        ]
        conflict_list = [
            ['ok', self.conflicted_file],
        ]
        self._merge_preview(
            resolved=False, conflict_list=conflict_list, cpr=True, warnings=warnings
        )
        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file, content=self.source_contents
        )
        self._check_file_content(recipe_dir_target_check, self.conflicted_file_new)

        # cleanup
        self._cleanup()

    def test_19_m_rma(self):
        self._init('19_m_rma')

        self._update(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file, self.source_contents
        )
        self._rename(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file,
            self.conflicted_file_new, self.target_contents
        )

        # do merge preview before resolving conflicts
        warnings = [
            "File '%s/%s': modified in source kitchen; renamed or deleted in target kitchen" %
            (self.recipe, self.conflicted_file)
        ]
        conflict_list = [
            ['conflict', self.conflicted_file],
        ]
        self._merge_preview(
            resolved=False, conflict_list=conflict_list, cpr=True, warnings=warnings
        )

        # Resolve the conflict
        self._resolve_conflict(self.conflicted_file, self.merge_contents)

        # do merge preview after resolving conflicts
        self._merge_preview(resolved=True, conflict_list=conflict_list)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file, content=self.merge_contents
        )
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new, content=self.target_contents
        )

        # cleanup
        self._cleanup()

    def test_22_rnca_nc(self):
        self._init('22_rnca_nc')

        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new
        )

        # do merge preview
        conflict_list = [
            ['ok', self.conflicted_file],
            ['ok', self.conflicted_file_new],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(recipe_dir_target_check, self.conflicted_file_new)

        # cleanup
        self._cleanup()

    def test_29_rma_nc(self):
        self._init('29_rma_nc')

        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new, self.source_contents
        )

        # do merge preview
        conflict_list = [
            ['ok', self.conflicted_file],
            ['ok', self.conflicted_file_new],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new, content=self.source_contents
        )

        # cleanup
        self._cleanup()

    def test_16_m_d(self):
        self._init('16_m_d')

        self._update(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file, self.source_contents
        )
        self._delete(self.target_kitchen, self.recipe_dir_target, self.conflicted_file)

        # do merge preview before resolving conflicts
        conflict_list = [
            ['conflict', self.conflicted_file],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # Resolve the conflict
        self._resolve_conflict(self.conflicted_file, self.merge_contents)

        # do merge preview after resolving conflicts
        self._merge_preview(resolved=True, conflict_list=conflict_list)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file_new)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file, content=self.merge_contents
        )

        # cleanup
        self._cleanup()

    def test_50_m_d_resolve_delete(self):
        self._init('50_m_d')

        self._update(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file, self.source_contents
        )
        self._delete(self.target_kitchen, self.recipe_dir_target, self.conflicted_file)

        # do merge preview before resolving conflicts
        conflict_list = [
            ['conflict', self.conflicted_file],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # Resolve the conflict
        merge_contents = ''
        self._resolve_conflict(self.conflicted_file, merge_contents)

        # do merge preview after resolving conflicts
        self._merge_preview(resolved=True, conflict_list=conflict_list)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file_new)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)

        # cleanup
        self._cleanup()

    def test_9_d_d(self):
        self._init('9_d_d')

        self._delete(self.source_kitchen, self.recipe_dir_source, self.conflicted_file)
        self._delete(self.target_kitchen, self.recipe_dir_target, self.conflicted_file)

        # do merge preview before resolving conflicts
        conflict_list = [
            ['ok', self.conflicted_file],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file_new)

        # cleanup
        self._cleanup()

    def test_11_d_rnca(self):
        self._init('11_d_rnca')

        self._delete(self.source_kitchen, self.recipe_dir_source, self.conflicted_file)
        self._rename(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file,
            self.conflicted_file_new
        )

        # do merge preview before resolving conflicts
        warnings = [
            "File '%s/%s': renamed or deleted in source kitchen; renamed to '%s/%s' in target kitchen"
            % (self.recipe, self.conflicted_file, self.recipe, self.conflicted_file_new)
        ]
        conflict_list = [
            ['ok', self.conflicted_file],
        ]
        self._merge_preview(
            resolved=False, conflict_list=conflict_list, cpr=True, warnings=warnings
        )

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(recipe_dir_target_check, self.conflicted_file_new)

        # cleanup
        self._cleanup()

    def test_10_d_m(self):
        self._init('10_d_m')

        self._delete(self.source_kitchen, self.recipe_dir_source, self.conflicted_file)
        self._update(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file, self.target_contents
        )

        # do merge preview before resolving conflicts
        conflict_list = [
            ['conflict', self.conflicted_file],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # Resolve the conflict
        self._resolve_conflict(self.conflicted_file, self.merge_contents)

        # do merge preview after resolving conflicts
        self._merge_preview(resolved=True, conflict_list=conflict_list)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file, content=self.merge_contents
        )
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file_new)

        # cleanup
        self._cleanup()

    def test_24_rnca_m(self):
        self._init('24_rnca_m')

        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new
        )
        self._update(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file, self.target_contents
        )

        # do merge preview before resolving conflicts
        conflict_list = [
            ['ok', self.conflicted_file_new],
            ['conflict', self.conflicted_file],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # Resolve the conflict
        self._resolve_conflict(self.conflicted_file, self.merge_contents)

        # do merge preview after resolving conflicts
        self._merge_preview(resolved=True, conflict_list=conflict_list)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file, content=self.merge_contents
        )
        self._check_file_content(recipe_dir_target_check, self.conflicted_file_new)

        # cleanup
        self._cleanup()

    def test_31_rma_m(self):
        self._init('31_rma_m')

        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new, self.source_contents
        )
        self._update(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file, self.target_contents
        )

        # do merge preview before resolving conflicts
        conflict_list = [
            ['ok', self.conflicted_file_new],
            ['conflict', self.conflicted_file],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # Resolve the conflict
        self._resolve_conflict(self.conflicted_file, self.merge_contents)

        # do merge preview after resolving conflicts
        self._merge_preview(resolved=True, conflict_list=conflict_list)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file, content=self.merge_contents
        )
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new, content=self.source_contents
        )

        # cleanup
        self._cleanup()

    def test_23_rnca_d(self):
        self._init('23_rnca_d')

        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new
        )
        self._delete(self.target_kitchen, self.recipe_dir_target, self.conflicted_file)

        # do merge preview before resolving conflicts
        warnings = [
            "File '%s/%s': renamed to '%s/%s' in source kitchen; renamed or deleted in target kitchen"
            % (self.recipe, self.conflicted_file, self.recipe, self.conflicted_file_new)
        ]

        conflict_list = [
            ['ok', self.conflicted_file],
            ['ok', self.conflicted_file_new],
        ]
        self._merge_preview(
            resolved=False, conflict_list=conflict_list, cpr=True, warnings=warnings
        )

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(recipe_dir_target_check, self.conflicted_file_new)

        # cleanup
        self._cleanup()

    def test_51_rnca_m_on_target(self):
        self._init('51_rnca_m_on_target')

        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new
        )
        self._update(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file_new,
            self.target_contents
        )

        # do merge preview before resolving conflicts
        conflict_list = [
            ['ok', self.conflicted_file],
            ['conflict', self.conflicted_file_new],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # Resolve the conflict
        self._resolve_conflict(self.conflicted_file_new, self.merge_contents)

        # do merge preview after resolving conflicts
        self._merge_preview(resolved=True, conflict_list=conflict_list)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new, content=self.merge_contents
        )

        # cleanup
        self._cleanup()

    def test_52_rnca_m_on_target_plus_delete(self):
        self._init('52_rnca_m_on_target_plus_delete')

        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new
        )
        self._update(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file_new,
            self.target_contents
        )
        self._delete(self.target_kitchen, self.recipe_dir_target, self.conflicted_file_new)

        # do merge preview before resolving conflicts
        conflict_list = [
            ['ok', self.conflicted_file],
            ['ok', self.conflicted_file_new],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(recipe_dir_target_check, self.conflicted_file_new)

        # cleanup
        self._cleanup()

    def test_30_rma_d(self):
        self._init('30_rma_d')

        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new, self.source_contents
        )
        self._delete(self.target_kitchen, self.recipe_dir_target, self.conflicted_file)

        # do merge preview before resolving conflicts
        warnings = [
            "File '%s/%s': renamed or deleted in source kitchen; renamed or deleted in target kitchen"
            % (self.recipe, self.conflicted_file)
        ]
        conflict_list = [
            ['ok', self.conflicted_file],
            ['ok', self.conflicted_file_new],
        ]
        self._merge_preview(
            resolved=False, conflict_list=conflict_list, cpr=True, warnings=warnings
        )

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new, content=self.source_contents
        )

        # cleanup
        self._cleanup()

    def test_53_rma_m_on_target_plus_delete(self):
        self._init('53_rma_m_on_target_plus_delete')

        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new, self.source_contents
        )
        self._update(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file_new,
            self.target_contents
        )
        self._delete(self.target_kitchen, self.recipe_dir_target, self.conflicted_file_new)

        # do merge preview before resolving conflicts
        conflict_list = [
            ['ok', self.conflicted_file],
            ['ok', self.conflicted_file_new],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new, content=self.source_contents
        )

        # cleanup
        self._cleanup()

    def test_27_rnca_rncb(self):
        self._init('27_rnca_rncb')

        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new
        )
        self._rename(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file,
            self.conflicted_file_new2
        )

        # do merge preview before resolving conflicts
        warnings = [
            "File '%s/%s': renamed to '%s/%s' in source kitchen; renamed to '%s/%s' in target kitchen"
            % (
                self.recipe, self.conflicted_file, self.recipe, self.conflicted_file_new,
                self.recipe, self.conflicted_file_new2
            )
        ]
        conflict_list = [
            ['ok', self.conflicted_file],
            ['ok', self.conflicted_file_new],
        ]
        self._merge_preview(
            resolved=False, conflict_list=conflict_list, cpr=True, warnings=warnings
        )

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(recipe_dir_target_check, self.conflicted_file_new)
        self._check_file_content(recipe_dir_target_check, self.conflicted_file_new2)

        # cleanup
        self._cleanup()

    def test_28_rnca_rmb(self):
        self._init('28_rnca_rmb')

        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new
        )
        self._rename(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file,
            self.conflicted_file_new2, self.target_contents
        )

        # do merge preview before resolving conflicts
        warnings = [
            "File '%s/%s': renamed to '%s/%s' in source kitchen; renamed or deleted in target kitchen"
            % (self.recipe, self.conflicted_file, self.recipe, self.conflicted_file_new)
        ]
        conflict_list = [
            ['ok', self.conflicted_file],
            ['ok', self.conflicted_file_new],
        ]
        self._merge_preview(
            resolved=False, conflict_list=conflict_list, cpr=True, warnings=warnings
        )

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(recipe_dir_target_check, self.conflicted_file_new)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new2, content=self.target_contents
        )

        # cleanup
        self._cleanup()

    def test_25_rnca_rnca(self):
        self._init('25_rnca_rnca')

        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new
        )
        self._rename(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file,
            self.conflicted_file_new
        )

        # do merge preview before resolving conflicts
        conflict_list = [
            ['ok', self.conflicted_file],
            ['ok', self.conflicted_file_new],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(recipe_dir_target_check, self.conflicted_file_new)

        # cleanup
        self._cleanup()

    def test_26_rnca_rma(self):
        self._init('26_rnca_rma')

        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new
        )
        self._rename(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file,
            self.conflicted_file_new, self.target_contents
        )

        # do merge preview before resolving conflicts
        conflict_list = [
            ['ok', self.conflicted_file],
            ['conflict', self.conflicted_file_new],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # Resolve the conflict
        self._resolve_conflict(self.conflicted_file_new, self.merge_contents)

        # do merge preview after resolving conflicts
        self._merge_preview(resolved=True, conflict_list=conflict_list)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new, content=self.merge_contents
        )

        # cleanup
        self._cleanup()

    def test_32_rma_rnca(self):
        self._init('32_rma_rnca')

        # rename the conflicted file in source kitchen
        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new, self.source_contents
        )

        # rename the conflicted file in target kitchen
        self._rename(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file,
            self.conflicted_file_new
        )

        # do merge preview before resolving conflicts
        conflict_list = [
            ['ok', self.conflicted_file],
            ['conflict', self.conflicted_file_new],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # Resolve the conflict
        self._resolve_conflict(self.conflicted_file_new, self.merge_contents)

        # do merge preview after resolving conflicts
        self._merge_preview(resolved=True, conflict_list=conflict_list)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new, content=self.merge_contents
        )

        # cleanup
        self._cleanup()

    def test_33_rma_rma(self):
        self._init('33_rma_rma')

        # rename the conflicted file in source kitchen
        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new, self.source_contents
        )

        # rename the conflicted file in target kitchen
        self._rename(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file,
            self.conflicted_file_new, self.target_contents
        )

        # do merge preview before resolving conflicts
        conflict_list = [
            ['ok', self.conflicted_file],
            ['conflict', self.conflicted_file_new],
        ]
        self._merge_preview(resolved=False, conflict_list=conflict_list, cpr=True)

        # Resolve the conflict
        self._resolve_conflict(self.conflicted_file_new, self.merge_contents)

        # do merge preview after resolving conflicts
        self._merge_preview(resolved=True, conflict_list=conflict_list)

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new, content=self.merge_contents
        )

        # cleanup
        self._cleanup()

    def test_34_rma_rncb(self):
        self._init('34_rma_rncb')

        # rename the conflicted file in source kitchen
        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new, self.source_contents
        )

        # rename the conflicted file in target kitchen
        self._rename(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file,
            self.conflicted_file_new2
        )

        # do merge preview before resolving conflicts
        warnings = [
            "File '%s/%s': renamed or deleted in source kitchen; renamed to '%s/%s' in target kitchen"
            % (self.recipe, self.conflicted_file, self.recipe, self.conflicted_file_new2)
        ]
        conflict_list = [
            ['ok', self.conflicted_file],
            ['ok', self.conflicted_file_new],
        ]
        self._merge_preview(
            resolved=False, conflict_list=conflict_list, cpr=True, warnings=warnings
        )

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new, content=self.source_contents
        )
        self._check_file_content(recipe_dir_target_check, self.conflicted_file_new2)

        # cleanup
        self._cleanup()

    def test_35_rma_rmb(self):
        self._init('35_rma_rmb')

        # rename the conflicted file in source kitchen
        self._rename(
            self.source_kitchen, self.recipe_dir_source, self.conflicted_file,
            self.conflicted_file_new, self.source_contents
        )

        # rename the conflicted file in target kitchen
        self._rename(
            self.target_kitchen, self.recipe_dir_target, self.conflicted_file,
            self.conflicted_file_new2, self.target_contents
        )

        # do merge preview before resolving conflicts
        warnings = [
            "File '%s/%s': renamed or deleted in source kitchen; renamed or deleted in target kitchen"
            % (self.recipe, self.conflicted_file)
        ]
        conflict_list = [
            ['ok', self.conflicted_file],
            ['ok', self.conflicted_file_new],
        ]
        self._merge_preview(
            resolved=False, conflict_list=conflict_list, cpr=True, warnings=warnings
        )

        # do merge
        self._merge(conflict_list=conflict_list)

        # check target recipe after merge
        temp_dir_target_check, kitchen_dir_target_check, recipe_dir_target_check = self._get_recipe(
            self.target_kitchen, self.recipe
        )
        self.temp_dirs.append(temp_dir_target_check)
        self._check_file_not_present(recipe_dir_target_check, self.conflicted_file)
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new, content=self.source_contents
        )
        self._check_file_content(
            recipe_dir_target_check, self.conflicted_file_new2, content=self.target_contents
        )

        # cleanup
        self._cleanup()

    # ------------------- helper methods -------------------------------------------------------------------------------
    def _init(self, merge_type):
        self.base_kitchen = 'CLI-Top'

        self.source_kitchen = 'merge_resolve_source_' + merge_type
        self.source_kitchen = self._add_my_guid(self.source_kitchen)
        self.target_kitchen = 'merge_resolve_target_' + merge_type
        self.target_kitchen = self._add_my_guid(self.target_kitchen)

        self.recipe = 'simple'

        self.conflicted_file = normalize('resources/very_cool.sql', WIN)
        self.conflicted_file_new = normalize('resources/deeper/very_cool_002.sql', WIN)
        self.conflicted_file_new2 = normalize('resources/deeper2/very_cool_002_2.sql', WIN)

        self.runner = CliRunner()

        self.temp_dirs = list()
        self._cleanup()

        time.sleep(BaseTestCloud.SLEEP_TIME)
        result = self.runner.invoke(
            dk, ['kitchen-create', '--parent', self.base_kitchen, self.source_kitchen]
        )
        self.assertEqual(0, result.exit_code, result.output)

        time.sleep(BaseTestCloud.SLEEP_TIME)
        result = self.runner.invoke(
            dk, ['kitchen-create', '--parent', self.source_kitchen, self.target_kitchen]
        )
        self.assertEqual(0, result.exit_code, result.output)

        # get target recipe
        self.temp_dir_target, self.kitchen_dir_target, self.recipe_dir_target = self._make_recipe_dir(
            self.recipe, self.target_kitchen
        )
        self.temp_dirs.append(self.temp_dir_target)
        os.chdir(self.kitchen_dir_target)
        result = self.runner.invoke(dk, ['recipe-get', self.recipe])
        self.assertEqual(0, result.exit_code, result.output)
        rv = result.output
        self.assertTrue(self.recipe in rv)
        self.assertTrue(os.path.exists(self.recipe))

        # get source recipe
        self.temp_dir_source, self.kitchen_dir_source, self.recipe_dir_source = self._make_recipe_dir(
            self.recipe, self.source_kitchen
        )
        self.temp_dirs.append(self.temp_dir_source)
        os.chdir(self.kitchen_dir_source)
        result = self.runner.invoke(dk, ['recipe-get', self.recipe])
        self.assertEqual(0, result.exit_code, result.output)
        rv = result.output
        self.assertTrue(self.recipe in rv)
        self.assertTrue(os.path.exists(self.recipe))

        self.source_contents = 'line1\nsource\nline2\n'
        self.source_contents2 = 'line1\nsource2\nline2\n'
        self.target_contents = 'line1\ntarget\nline2\n'
        self.merge_contents = 'line1\nmerged\nline2\n'

    def _update(self, kitchen, recipe_dir, file_path, content):
        os.chdir(recipe_dir)
        path, file_name = os.path.split(file_path)
        if not os.path.exists(path):
            os.makedirs(path)
        with open(file_path, 'w+') as f:
            f.write(content)
        message = 'adding %s to %s' % (file_path, kitchen)
        result = self.runner.invoke(
            dk, [
                'file-update', '--kitchen', kitchen, '--recipe', self.recipe, '--message', message,
                file_path
            ]
        )
        self.assertEqual(0, result.exit_code, result.output)

    def _rename(self, kitchen, recipe_dir, file_path, file_new_path, content=None):
        os.chdir(recipe_dir)
        if content:
            with open(file_path, 'w') as f:
                f.write(content)
        file_full = os.path.join(recipe_dir, file_path)
        file_new_path_full = os.path.join(recipe_dir, file_new_path)
        head, tail = os.path.split(file_new_path_full)
        os.mkdir(head)
        shutil.move(file_full, file_new_path_full)
        message = 'renaming %s to %s into kitchen %s' % (file_path, file_new_path, kitchen)
        result = self.runner.invoke(dk, ['recipe-update', '-d', '--message', message])
        self.assertEqual(0, result.exit_code, result.output)

    def _delete(self, kitchen, recipe_dir, file_path):
        # delete the conflicted file in kitchen
        os.chdir(recipe_dir)
        os.remove(file_path)
        message = 'deleting %s into kitchen %s' % (file_path, kitchen)
        result = self.runner.invoke(dk, ['recipe-update', '-d', '--message', message])
        self.assertEqual(0, result.exit_code, result.output)

        # re get source recipe to clean possible empty directories
        result = self.runner.invoke(dk, ['recipe-get', self.recipe, '-y', '-o', '-d'])
        rv = result.output
        self.assertTrue(self.recipe in rv)
        self.assertEqual(0, result.exit_code, result.output)

    def _get_recipe(self, kitchen, recipe):
        temp_dir, kitchen_dir, recipe_dir = self._make_recipe_dir(recipe, kitchen)
        os.chdir(kitchen_dir)
        result = self.runner.invoke(dk, ['recipe-get', recipe])
        rv = result.output
        self.assertTrue(recipe in rv)
        self.assertTrue(os.path.exists(recipe))
        return temp_dir, kitchen_dir, recipe_dir

    def _cleanup(self):
        os.chdir(self._api.get_merge_dir())
        self.runner.invoke(dk, ['kitchen-delete', self.source_kitchen, '--yes'])
        self.runner.invoke(dk, ['kitchen-delete', self.target_kitchen, '--yes'])
        for temp_dir in self.temp_dirs:
            shutil.rmtree(temp_dir, ignore_errors=True)

    def _merge_preview(
            self, resolved=False, conflict_list=None, cpr=False, reverse=False, warnings=None
    ):
        os.chdir(self.temp_dir_source)
        if reverse:
            command = [
                'kitchen-merge-preview', '--source_kitchen', self.target_kitchen,
                '--target_kitchen', self.source_kitchen
            ]
        else:
            command = [
                'kitchen-merge-preview', '--source_kitchen', self.source_kitchen,
                '--target_kitchen', self.target_kitchen
            ]
        if cpr:
            command.append('-cpr')
        result = self.runner.invoke(dk, command)
        self.assertEqual(0, result.exit_code, result.output)

        if resolved:
            for conflict in conflict_list:
                if conflict[0] == 'conflict':
                    conflict[0] = 'resolved'

        if conflict_list:
            for conflict in conflict_list:
                status = conflict[0]
                file_path = conflict[1]
                file_path_with_recipe = os.path.join(self.recipe, file_path)
                text = "%s\t\t%s" % (status.rjust(8), file_path_with_recipe)
                self.assertTrue(text in result.output, result.output)
        else:
            text = 'Nothing to merge.'
            self.assertTrue(text in result.output, result.output)
        splitted_output = result.output.split('\n')

        if warnings:
            for line in warnings:
                self.assertTrue(line.replace("\\", "/") in result.output, result.output)

        index = 0
        stage = 1
        while index < len(splitted_output):
            if stage == 1:
                if 'Previewing merge Kitchen' in splitted_output[index]:
                    stage += 1
                index += 1
                continue
            if stage == 2:
                if 'Merge Preview Results' in splitted_output[index]:
                    stage += 1
                index += 1
                continue
            if stage == 3:
                if 'Kitchen merge preview done.' in splitted_output[index]:
                    stage += 1
                index += 1
                continue
            index += 1

        self.assertEqual(4, stage, result.output)

    def _resolve_conflict(self, file_path, merge_contents):
        os.chdir(self.temp_dir_source)

        # write file
        full_merge_path = self._get_full_merge_path(file_path)
        with open('%s.base' % full_merge_path, 'w') as f:
            f.write(merge_contents)

        result = self.runner.invoke(
            dk, [
                'file-resolve', '--source_kitchen', self.source_kitchen, '--target_kitchen',
                self.target_kitchen,
                os.path.normpath('simple/%s' % file_path)
            ]
        )
        self.assertEqual(0, result.exit_code, result.output)
        self.assertTrue('File resolve done.' in result.output)

        resolved_contents = DKFileHelper.read_file('%s.resolved' % full_merge_path
                                                   ).replace('\r', '')
        self.assertEqual(merge_contents, resolved_contents)

    def _get_full_merge_path(self, file_path):
        base_working_dir = self._api.get_merge_dir()
        path1 = '%s' % base_working_dir
        path2 = '%s_to_%s' % (self.source_kitchen, self.target_kitchen)
        working_dir = os.path.join(path1, path2)
        return os.path.join(working_dir, self.recipe, file_path)

    def _merge(self, conflict_list=None, nothing_to_do=False, reverse=False):
        os.chdir(self.temp_dir_source)
        if reverse:
            result = self.runner.invoke(
                dk, [
                    'kitchen-merge', '--source_kitchen', self.target_kitchen, '--target_kitchen',
                    self.source_kitchen, '--yes'
                ]
            )
        else:
            result = self.runner.invoke(
                dk, [
                    'kitchen-merge', '--source_kitchen', self.source_kitchen, '--target_kitchen',
                    self.target_kitchen, '--yes'
                ]
            )
        if nothing_to_do:
            self.assertEqual(1, result.exit_code, result.output)
            text = 'Already up to date. Nothing to do.'
            self.assertTrue(text in result.output, result.output)
            return

        self.assertEqual(0, result.exit_code, result.output)

        has_conflicts = False

        if conflict_list:
            for conflict in conflict_list:
                if conflict[0] == 'resolved':
                    has_conflicts = True
                    full_merge_path = self._get_full_merge_path(conflict[1])
                    text = 'Found %s.resolved' % full_merge_path
                    self.assertTrue(text in result.output, result.output)

        splitted_output = result.output.split('\n')

        if has_conflicts:
            calling_merge = 'Calling Merge with manual resolved conflicts ...'
        else:
            calling_merge = 'Calling Merge ...'

        index = 0
        stage = 1
        while index < len(splitted_output):
            if stage == 1:
                if 'looking for manually merged files' in splitted_output[index]:
                    stage += 1
                index += 1
                continue
            if stage == 2:
                if calling_merge in splitted_output[index]:
                    stage += 1
                index += 1
                continue
            if stage == 3:
                if 'Merge done.' in splitted_output[index]:
                    stage += 1
                index += 1
                continue
            if stage == 4:
                url = '/dk/index.html#/history/dk/'
                if 'Url:' in splitted_output[index] and url in splitted_output[index]:
                    stage += 1
                index += 1
                continue

            index += 1

        self.assertEqual(5, stage, result.output)

    def _check_file_content(self, recipe_dir, file_name, content=None):
        full_path = os.path.join(recipe_dir, file_name)
        actual_content = DKFileHelper.read_file(full_path).replace('\r', '')
        if content:
            self.assertEqual(actual_content, content, 'path: %s' % recipe_dir)
        else:
            self.assertTrue('select 1' in actual_content, 'path: %s' % recipe_dir)

    def _check_file_not_present(self, recipe_dir, file_name):
        full_path = os.path.join(recipe_dir, file_name)
        self.assertFalse(os.path.exists(full_path))


if __name__ == '__main__':
    unittest.main()
