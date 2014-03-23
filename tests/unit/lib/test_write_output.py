import os
# Remove file with os.remove
import shutil
# Remove directory and contents with shutil.rmtree

try:
    import unittest2 as unittest
except:
    import unittest

from testfixtures import LogCapture

from tests.test_objects.tobject import TObject
from tests.test_objects.row_proxy import RowProxy

test_file_directory = './tests/test_files/'

# We need to wrap everything after the output_to_file into a try...finally in
#   order to properly delete things. Should look into a cleanup function
#   when the class is done executing

class TestOutputToFile(unittest.TestCase):
    """
    This class is meant to test the output_to_file function
    """
    
    def _clean_up_file(self, file_path):
        os.remove(file_path)


    def _assert_length(self, file_path, expected_length):
        f = open(file_path, 'r')
        o = f.read().splitlines()

        assert len(o) == expected_length
    

    def test_simple_write(self):
        from outlib.lib.wout import output_to_file
        file_path = "%s%s" % (test_file_directory, 'test_simple_write.txt')

        output = "This is a test\n"

        output_to_file(file_path, output)
         
        try:
            self._assert_length(file_path, 1)
        finally:
            self._clean_up_file(file_path)


    def test_simple_append(self):
        from outlib.lib.wout import output_to_file
        file_path = "%s%s" % (test_file_directory, 'test_simple_append.txt')

        output = "This is a test\n"

        output_to_file(file_path, output, append=True)

        try:
            self._assert_length(file_path, 1)
        finally:
            self._clean_up_file(file_path)

    
    def test_simple_write_twice(self):
        from outlib.lib.wout import output_to_file
        file_path = "%s%s" % (test_file_directory, 'test_simple_write_twice.txt')

        output = 'This is a test\n'

        output_to_file(file_path, output)
        output_to_file(file_path, output)

        try:
            self._assert_length(file_path, 1)
        finally:
            self._clean_up_file(file_path)


    def test_simple_append_twice(self):
        from outlib.lib.wout import output_to_file
        file_path = "%s%s" % (test_file_directory, 'test_simple_append_twice.txt')

        output = 'This is a test\n'

        output_to_file(file_path, output, append=True)
        output_to_file(file_path, output, append=True)

        try:
            self._assert_length(file_path, 2)
        finally:
            self._clean_up_file(file_path)


    def test_dict_write_simple(self):
        from outlib.lib.wout import output_to_file
        file_path = "%s%s" % (test_file_directory, 'test_dict_write_simple.txt')

        output = {'a': 'cool'}

        output_to_file(file_path, output)

        try:
            self._assert_length(file_path, 3)
        finally:
            self._clean_up_file(file_path)


    def test_dict_write_one_inside_another(self):
        from outlib.lib.wout import output_to_file
        file_path = "%s%s" % (test_file_directory, 'test_dict_write_one_inside_another.txt')

        output = {'a': 'cool', 'b': {'c': '45'}}

        output_to_file(file_path, output)

        try:
            self._assert_length(file_path, 6)
        finally:
            self._clean_up_file(file_path)

    
    def test_dict_write_one_inside_another_with_int_value(self):
        from outlib.lib.wout import output_to_file
        file_path = "%s%s" % (test_file_directory, 'test_dict_write_one_inside_another.txt')

        output = {'a': 'cool', 'b': {'c': 45}}

        output_to_file(file_path, output)

        try:
            self._assert_length(file_path, 6)
        finally:
            self._clean_up_file(file_path)


    def test_list_write_simple(self):
        from outlib.lib.wout import output_to_file
        file_path = "%s%s" % (test_file_directory, 'test_list_write_simple.txt')

        output = ['1', '2']

        output_to_file(file_path, output)

        try:
            self._assert_length(file_path, 4)
        finally:
            self._clean_up_file(file_path)


    def test_list_write_dict_inside(self):
        from outlib.lib.wout import output_to_file
        file_path = "%s%s" % (test_file_directory, 'test_list_write_simple.txt')

        output = ['1', '2', {'a': 'beee'}]

        output_to_file(file_path, output)

        try:
            self._assert_length(file_path, 7)
        finally:
            self._clean_up_file(file_path)


    def test_list_write_list_inside(self):
        from outlib.lib.wout import output_to_file
        file_path = "%s%s" % (test_file_directory, 'test_list_write_simple.txt')

        output = ['1', '2', [3, 4]]

        output_to_file(file_path, output)

        try:
            self._assert_length(file_path, 8)
        finally:
            self._clean_up_file(file_path)


    def test_list_write_obj_inside(self):
        from outlib.lib.wout import output_to_file
        file_path = "%s%s" % (test_file_directory, 'test_list_write_simple.txt')

        output = ['1', '2', TObject(test='test')]

        output_to_file(file_path, output)

        try:
            self._assert_length(file_path, 7)
        finally:
            self._clean_up_file(file_path)


    def test_object_write_simple(self):
        from outlib.lib.wout import output_to_file
        file_path = "%s%s" % (test_file_directory, 'test_obj_write_simple.txt')

        output = TObject(test='test')

        output_to_file(file_path, output)

        try:
            self._assert_length(file_path, 3)
        finally:
            self._clean_up_file(file_path)
    

    def test_object_write_obj_inside_another(self):
        from outlib.lib.wout import output_to_file
        file_path = "%s%s" % (test_file_directory, 'test_obj_write_obj_inside_another.txt')

        output = TObject(test='test', test2= {'c': '45'})

        output_to_file(file_path, output)

        try:
            self._assert_length(file_path, 6)
        finally:
            self._clean_up_file(file_path)
    

    def test_object_write_obj_2_inside_another(self):
        from outlib.lib.wout import output_to_file
        file_path = "%s%s" % (test_file_directory, 'test_obj_write_obj_2_inside_another.txt')

        output = TObject(test='test', test2= {'c': '45'}, test3= {'d': {'e': 1, 'f': '3'}})

        output_to_file(file_path, output)

        try:
            self._assert_length(file_path, 12)
        finally:
            self._clean_up_file(file_path)


    def test_row_proxy_write_simple(self):
        from outlib.lib.wout import output_to_file
        file_path = "%s%s" % (test_file_directory, 'test_obj_write_obj_inside_another.txt')

        output = RowProxy(test='test', test2= 45)

        output_to_file(file_path, output)

        try:
            self._assert_length(file_path, 4)
        finally:
            self._clean_up_file(file_path)


    def test_row_proxy_write_list(self):
        from outlib.lib.wout import output_to_file
        file_path = "%s%s" % (test_file_directory, 'test_obj_write_obj_inside_another.txt')

        output = []
        output.append(RowProxy(key1='test1', key11= 1))
        output.append(RowProxy(key2='test2', key22= '45'))
        output.append(RowProxy(key3='test3', key33= 3))

        output_to_file(file_path, output)

        try:
            self._assert_length(file_path, 14)
        finally:
            self._clean_up_file(file_path)


class TestOutputToLogger(unittest.TestCase):
    """
    This class is meant to test the output_to_logger function
    """
    
    def test_log_simple(self):
        from outlib.lib.wout import output_to_logger

        with LogCapture() as l:
            output_to_logger('This is a Test')

        assert l.check(('root', 'INFO', '\n\nThis is a Test\n\n'))


