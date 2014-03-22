try:
    import unittest2 as unittest
except:
    import unittest

test_file_directory = './tests/test_files/'

class TestWriteOutput(unittest.TestCase):
    
    def test_single_variable(self):
        from outlib.lib.write_output import write_output
        file_path = "%s%s" % (test_file_directory, 'test_single_variable.txt')
        write_output(file_path, 'This is a test\n')
        assert 0 == 0
