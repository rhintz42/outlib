import os
import shutil

try:
    import unittest2 as unittest
except:
    import unittest

test_file_directory = './tests/test_files/'

# We need to wrap everything after the write_output into a try...finally in
#   order to properly delete things. Should look into a cleanup function
#   when the class is done executing

class TestWriteOutput(unittest.TestCase):
    
    def _clean_up_file(self, file_path):
        os.remove(file_path)

    def _assert_length(self, file_path, expected_length):
        f = open(file_path, 'r')
        o = f.read().splitlines()

        assert len(o) == expected_length
    
    def test_simple_write(self):
        from outlib.lib.write_output import write_output
        file_path = "%s%s" % (test_file_directory, 'test_simple_write.txt')

        output = "This is a test\n"

        try:
            write_output(file_path, output)
            
            self._assert_length(file_path, 1)
        finally:
            self._clean_up_file(file_path)

    def test_simple_append(self):
        from outlib.lib.write_output import write_output
        file_path = "%s%s" % (test_file_directory, 'test_simple_append.txt')

        output = "This is a test\n"

        try:
            write_output(file_path, output, append=True)

            self._assert_length(file_path, 1)
        finally:
            self._clean_up_file(file_path)
    
    def test_simple_write_twice(self):
        from outlib.lib.write_output import write_output
        file_path = "%s%s" % (test_file_directory, 'test_simple_write_twice.txt')

        output = 'This is a test\n'

        try:
            write_output(file_path, output)
            write_output(file_path, output)

            self._assert_length(file_path, 1)
        finally:
            self._clean_up_file(file_path)

    def test_simple_append_twice(self):
        from outlib.lib.write_output import write_output
        file_path = "%s%s" % (test_file_directory, 'test_simple_append_twice.txt')

        output = 'This is a test\n'

        try:
            write_output(file_path, output, append=True)
            write_output(file_path, output, append=True)

            self._assert_length(file_path, 2)
        finally:
            self._clean_up_file(file_path)
