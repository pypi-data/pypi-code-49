#!/usr/bin/env python3
"""Test basic python utility functions """
########################################################################
# File: utils_test.py
#  executable: utils_test.py

# Author: Andrew Bailey
# History: 12/07/17 Created
########################################################################
import unittest
import tempfile
import filecmp

from py3helpers.utils import *


class UtilsTests(unittest.TestCase):
    """Test the functions in all of utils"""

    @classmethod
    def setUpClass(cls):
        super(UtilsTests, cls).setUpClass()
        cls.HOME = '/'.join(os.path.abspath(__file__).split("/")[:-2])

    def test_time_it(self):
        """Test time_it function"""
        with captured_output() as (_, _):
            def add(x, y):
                return x + y

            _, _ = time_it(add, 1, 2)
            with self.assertRaises(AssertionError):
                time_it(1, 1, 2)

    def test_list_dir(self):
        """Test list_dir function"""
        with captured_output() as (_, _):
            fake_path = "asdf/adsf/"
            fake_str = 0
            with self.assertRaises(AssertionError):
                list_dir(fake_str)
                list_dir(fake_path)
            with tempfile.TemporaryDirectory() as tempdir:
                path = os.path.join(tempdir, "test.csv")
                with open(path, "w") as tmp:
                    files = list_dir(tempdir)
                    self.assertEqual(files[0], path)
                    files = list_dir(tempdir, ext='tsv')
                    self.assertEqual(files, [])

    def test_create_logger(self):
        """Test create_logger"""
        with self.assertRaises(AssertionError):
            create_logger("asdf", "a", info="asdf")
        with tempfile.TemporaryDirectory() as tempdir:
            with self.assertRaises(AssertionError):
                create_logger(tempdir, "a", info="asdf")
                create_logger(tempdir, 1, info=True)
            with captured_output() as (out, err):
                path = os.path.join(tempdir, "test")
                log1 = create_logger(path, "b")
                log1.warning("test")
                log1.debug("Don't print to console")
                output = err.getvalue().split()[-1]
                self.assertEqual(output, 'test')
                log2 = create_logger(path, "a", debug=True)
                log2.debug("test1")
                output = err.getvalue().split()[-1]
                self.assertEqual(output, 'test1')
                last_words = ["test", "console", "test1"]
            with open(path + ".log", 'r') as fh:
                for indx, line in enumerate(fh):
                    last_word = line.split()[-1]
                    self.assertEqual(last_word, last_words[indx])

    def test_merge_two_dicts(self):
        """Test merge_two_dicts"""
        with captured_output() as (_, _):
            self.assertRaises(AssertionError, merge_two_dicts, {"test": 1}, "test")
            self.assertRaises(AssertionError, merge_two_dicts, {"test": 1}, 1)
            self.assertRaises(AssertionError, merge_two_dicts, ["test", 1], {"test": 1})
            dict1 = {"a": 1}
            dict2 = {"b": 2}
            merge_dict = merge_two_dicts(dict1, dict2)
            self.assertEqual(dict1["a"], merge_dict["a"])
            self.assertEqual(dict2["b"], merge_dict["b"])

    def test_merge_dicts(self):
        """Test merge_dicts"""
        with captured_output() as (_, _):
            self.assertRaises(AssertionError, merge_dicts, {"test": 1})
            self.assertRaises(AssertionError, merge_dicts, ["test", 1])
            self.assertRaises(AssertionError, merge_dicts, [{"test": 1}, ["test"]])

            dict1 = {"a": 1}
            dict2 = {"b": 2}
            dict3 = {"c": 3}
            dict4 = {"d": 4}

            merged_dict = merge_dicts([dict1, dict2, dict3, dict4])
            self.assertEqual(dict1["a"], merged_dict["a"])
            self.assertEqual(dict2["b"], merged_dict["b"])
            self.assertEqual(dict3["c"], merged_dict["c"])
            self.assertEqual(dict4["d"], merged_dict["d"])

    def test_check_numpy_table(self):
        """Test check_numpy_table method"""
        with captured_output() as (_, _):
            new = np.empty(3, dtype=[('reference_index', int), ('event_index', int),
                                     ('posterior_probability', float)])
            check_numpy_table(new, req_fields=["reference_index", 'event_index', 'posterior_probability'])

            with self.assertRaises(KeyError):
                check_numpy_table(new, req_fields=["something", 'event_index', 'posterior_probability'])
                check_numpy_table(new, req_fields=["something"])
            with self.assertRaises(TypeError):
                check_numpy_table('1', req_fields=["event_index"])

    def test_captured_output(self):
        """Test captured_output method"""
        string1 = "Something"
        string2 = "Else"
        with captured_output() as (out, err):
            print(string1, file=sys.stdout)
            print(string2, file=sys.stderr)
        self.assertEqual(out.getvalue(), "Something\n")
        self.assertEqual(err.getvalue(), "Else\n")

    def test_DotDict(self):
        with captured_output() as (_, _):
            dict1 = {"a": 1, "b": 2, 3: "c", "d": {"e": 4}}
            self.assertRaises(AssertionError, create_dot_dict, dict1)
            dict1 = {"a": 1, "b": 2, "d": {"e": 4}}
            dict2 = DotDict(dict1)
            self.assertEqual(dict2.a, 1)
            self.assertEqual(dict2.b, 2)
            self.assertEqual(dict2.d, {"e": 4})

    def test_create_dot_dict(self):
        with captured_output() as (_, _):
            dict1 = {"a": 1, "b": 2, 3: "c", "d": {"e": 4}}
            self.assertRaises(AssertionError, create_dot_dict, dict1)
            self.assertRaises(TypeError, create_dot_dict, [1, 2, 3])

            dict1 = {"a": 1, "b": 2, "d": {"e": 4}, "f": [{"g": 5, "h": 6}]}
            dict2 = create_dot_dict(dict1)
            self.assertEqual(dict2.a, 1)
            self.assertEqual(dict2.b, 2)
            self.assertEqual(dict2.d, {"e": 4})
            self.assertEqual(dict2.d.e, 4)
            self.assertEqual(dict2.f[0].g, 5)

    # TODO
    def test_load_json(self):
        """Test load_json method"""
        with captured_output() as (_, _):
            pass

    # TODO
    def test_save_json(self):
        """Test save_json method"""
        with captured_output() as (_, _):
            pass

    def test_change_np_field_type(self):
        """Test change_np_field_type method"""
        with captured_output() as (_, _):
            # create structured array
            old = np.zeros((10,), dtype=[("test", int)])
            new = change_np_field_type(old, "test", float)
            # same column is new data type
            self.assertIs(new.dtype["test"], np.dtype(float))
            # check passing wrong arguments
            self.assertRaises(AssertionError, change_np_field_type, np.zeros(1), "this", float)
            self.assertRaises(AssertionError, change_np_field_type, new, "this", float)
            self.assertRaises(TypeError, change_np_field_type, new, "test", "string")

    def test_all_string_permutations(self):
        """Test allLexicographic"""
        with captured_output() as (_, _):
            for x in range(1, 10):
                test_string = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
                generator = all_string_permutations(test_string, length=x)
                all_kmers = []
                for kmer in generator:
                    all_kmers.append(kmer)
                self.assertEqual(all_kmers, sorted(all_kmers))
                num_chars = len(set(test_string))
                self.assertEqual(num_chars ** x, len(all_kmers))
            self.assertRaises(AssertionError, all_string_permutations, "")
            self.assertRaises(AssertionError, all_string_permutations, "AT", 0)

    def test_allLexicographicRecur(self):
        """Test allLexicographic"""
        with captured_output() as (_, _):
            generator = allLexicographicRecur("ACGT", [''] * 4, 3, 0)
            all_kmers = []
            for x in generator:
                all_kmers.append(x)
            self.assertEqual(all_kmers, sorted(all_kmers))
            generator = allLexicographicRecur("AG", [''] * 4, 3, 0)
            all_kmers = []
            for x in generator:
                all_kmers.append(x)
            self.assertEqual(all_kmers, sorted(all_kmers))

    def test_get_random_string(self):
        """Test get_random_string"""
        with captured_output() as (_, _):
            test_string = get_random_string(5, "AAAA")
            self.assertEqual(test_string, "AAAAA")
            test_string = get_random_string(5, "ATGC")
            self.assertEqual(len(test_string), 5)
            self.assertTrue(set(test_string).issubset(set("ATGC")))

    def test_find_subsequence_indices(self):
        with captured_output() as (_, _):
            # no substrings
            indices = find_substring_indices("AAAAA", 'G', offset=0, overlap=True)
            self.assertEqual([x for x in indices], [])
            # yes substrings
            indices = find_substring_indices("AAAAA", 'A', offset=0, overlap=True)
            self.assertEqual([x for x in indices], [0, 1, 2, 3, 4])
            indices = find_substring_indices("AAAAA", 'AA', offset=0, overlap=True)
            self.assertEqual([x for x in indices], [0, 1, 2, 3])
            # test overlap
            indices = find_substring_indices("AAAAA", 'AA', offset=0, overlap=False)
            self.assertEqual([x for x in indices], [0, 2])
            # test offset
            indices = find_substring_indices("ATGCATGC", 'ATGCATGC', offset=1, overlap=True)
            self.assertEqual([x for x in indices], [1])
            indices = find_substring_indices("ATGCATGC", 'ATGCATGC', offset=1, overlap=True)
            self.assertEqual([x for x in indices], [1])
            # compare with gatc modtifs
            indices2 = find_substring_indices("gatcgatc", 'gatc', offset=1, overlap=True)
            self.assertEqual([x for x in indices2], [1, 5])
            # if empty string passed
            indices2 = find_substring_indices("", 'gatc', offset=1, overlap=True)
            self.assertRaises(AssertionError, indices2.__next__)
            indices2 = find_substring_indices("gatcgatc", '', offset=1, overlap=True)
            self.assertRaises(AssertionError, indices2.__next__)

    def test_merge_lists(self):
        with captured_output() as (_, _):
            a = [[1, 2, 3], [4, 5, 6]]
            self.assertEqual(merge_lists(a), [1, 2, 3, 4, 5, 6])

    def test_count_lines_in_file(self):
        with captured_output() as (_, _):
            n_lines = 100
            with tempfile.TemporaryDirectory() as tempdir:
                path = os.path.join(tempdir, "test.csv")
                with open(path, "w") as tmp:
                    for x in range(n_lines):
                        tmp.write("some_line\n")
                n_lines_in_file = count_lines_in_file(path)
                self.assertEqual(n_lines, n_lines_in_file)

    def test_all_abspath(self):
        with captured_output() as (_, _):
            self.assertIsNone(all_abspath(None))
            self.assertIsNotNone(all_abspath("path"))

    def test_split_every_string(self):
        with captured_output() as (_, _):
            a = "stringstringstring"
            for x in split_every_string(6, a):
                self.assertEqual(x, "string")

    def test_split_every(self):
        with captured_output() as (_, _):
            a = "stringstringstring"
            for x in split_every(6, a):
                self.assertEqual(x, list("string"))

    def test_list_dir_recursive(self):
        with captured_output() as (_, _):
            n_files = 0
            for file_path in list_dir_recursive(os.path.join(self.HOME, "tests"), ext="py"):
                n_files += 1
                self.assertTrue(file_path.endswith("py"))
            self.assertEqual(n_files, 7)

    def test_get_all_sub_directories(self):
        with captured_output() as (_, _):
            n_dirs = 0
            for _ in get_all_sub_directories(os.path.join(self.HOME, "tests")):
                n_dirs += 1
            self.assertEqual(n_dirs, 2)

    def test_binary_search_exact_match(self):
        with captured_output() as (_, _):
            for x in range(100, 1000, 10):
                test_list = list(range(x))
                time_list = []
                for _ in range(100):
                    find_number = np.random.randint(0, x)
                    index, time = time_it(binary_search, test_list, find_number)
                    time_list.append(time)
                    self.assertEqual(test_list[index], find_number)

    def test_binary_search_no_match(self):
        with captured_output() as (_, _):
            for x in range(10, 100, 10):
                test_list = list(range(x))
                time_list = []
                for _ in range(100):
                    find_number = np.random.randint(0, x) + 0.5
                    index, time = time_it(binary_search, test_list, find_number, False)
                    time_list.append(time)
                    if index == x - 1:
                        self.assertTrue(test_list[index] < find_number)
                    elif index == 0:
                        self.assertTrue(find_number < test_list[index+1])
                    else:
                        self.assertTrue(test_list[index] < find_number < test_list[index+1])

    def test_get_random_strings(self):
        with captured_output() as (_, _):
            string_len = 10
            for n_strings in range(10, 100, 10):
                all_strings = get_random_strings(n_strings, string_len)
                self.assertEqual(len(all_strings), n_strings)
                for string1 in all_strings:
                    self.assertEqual(len(string1), string_len)
            self.assertRaises(AssertionError, get_random_strings, 1000, 1)
            all_strings = get_random_strings(4**5, 5, chars="ATGC")
            self.assertEqual(len(all_strings), 4**5)

    def test_tar_gz(self):
        with captured_output() as (_, _):
            input_dir = os.path.join(self.HOME, "tests/test_files/test_tar_dir")
            dir_data = os.path.join(self.HOME, "tests/test_files/test_tar_dir/test.fa")
            with tempfile.TemporaryDirectory() as tempdir:
                # tempdir = "/Users/andrewbailey/CLionProjects/python_utils/py3helpers/tests/test_files/test_test_test"
                path = os.path.join(tempdir, "test.tgz")
                out_file = tar_gz(input_dir, path)
                path = untar_gz(out_file, out_dir=tempdir)
                output_dir = os.path.join(path, "test_tar_dir")
                self.assertTrue(filecmp.cmp(list_dir(output_dir)[0], dir_data))
                # test output to directory
                out_file = tar_gz(input_dir, tempdir)
                path = untar_gz(out_file, out_dir=tempdir)
                output_dir = os.path.join(path, "test_tar_dir")
                self.assertTrue(filecmp.cmp(list_dir(output_dir)[0], dir_data))

    def test_convert_seconds(self):
        with captured_output() as (_, _):
            n_seconds = 10.123412341234
            d, h, m, s = convert_seconds(n_seconds)
            self.assertEqual(0, d)
            self.assertEqual(0, h)
            self.assertEqual(0, m)
            self.assertEqual(10, s)
            n_seconds = 70.123412341234
            d, h, m, s = convert_seconds(n_seconds)
            self.assertEqual(0, d)
            self.assertEqual(0, h)
            self.assertEqual(1, m)
            self.assertEqual(10, s)
            n_seconds = 3610.123412341234
            d, h, m, s = convert_seconds(n_seconds)
            self.assertEqual(0, d)
            self.assertEqual(1, h)
            self.assertEqual(0, m)
            self.assertEqual(10, s)
            n_seconds = 86410.123412341234
            d, h, m, s = convert_seconds(n_seconds)
            self.assertEqual(1, d)
            self.assertEqual(0, h)
            self.assertEqual(0, m)
            self.assertEqual(10, s)

    def test_NestedDefaultDict(self):
        with captured_output() as (_, _):
            test_dict = NestedDefaultDict()
            for x in list("a"):
                self.assertEqual(test_dict[x], {})
                self.assertEqual(test_dict[x][x], {})
                self.assertEqual(test_dict[x][x], {})
                self.assertEqual(test_dict[x][x][x][x], {})
                self.assertEqual(test_dict[x][x][x][x][x], {})

    def test_concatenate_files(self):
        with captured_output() as (_, _):
            with tempfile.TemporaryDirectory() as tempdir:
                path = os.path.join(tempdir, "out.fa")
                test_fa = os.path.join(self.HOME, "tests/test_files/test_tar_dir/test.fa")
                concatenate_files([path, test_fa], path)
                self.assertEqual(os.stat(path).st_size, os.stat(test_fa).st_size)


if __name__ == '__main__':
    unittest.main()
