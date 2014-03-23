try:
    import unittest2 as unittest
except:
    import unittest

from tests.test_objects.tobject import TObject
from tests.test_objects.row_proxy import RowProxy

test_file_directory = './tests/test_files/'

# We need to wrap everything after the output_to_file into a try...finally in
#   order to properly delete things. Should look into a cleanup function
#   when the class is done executing

class TestFormatDict(unittest.TestCase):

    def test_dict_simple(self):
        from outlib.lib.format_vals import _format_dict

        input_val = {'a': 'b'}

        output = _format_dict(input_val)
         
        assert output['a'] == 'b'


    def test_dict_int_value(self):
        from outlib.lib.format_vals import _format_dict

        input_val = {'a': 1}

        output = _format_dict(input_val)
         
        assert output['a'] == 1


    def test_dict_dict_value(self):
        from outlib.lib.format_vals import _format_dict

        input_val = {'a': {'b': 'c'}}

        output = _format_dict(input_val)
         
        assert output['a']['b'] == 'c'


    def test_dict_list_value(self):
        from outlib.lib.format_vals import _format_dict

        input_val = {'a': ['b', 'c']}

        output = _format_dict(input_val)
         
        assert output['a'][0] == 'b'


    def test_dict_object_value(self):
        from outlib.lib.format_vals import _format_dict

        input_val = {'a': TObject(test1='value1')}

        output = _format_dict(input_val)
         
        assert output['a']['test1'] == 'value1'


    def test_dict_row_proxy_value(self):
        from outlib.lib.format_vals import _format_dict

        input_val = {'a': RowProxy(test1='value2')}

        output = _format_dict(input_val)
         
        assert output['a']['test1'] == 'value2'



class TestFormatList(unittest.TestCase):

    def test_list_simple(self):
        from outlib.lib.format_vals import _format_list

        input_val = ['a', 'b']

        output = _format_list(input_val)
         
        assert output[1] == 'b'


    def test_list_int_value(self):
        from outlib.lib.format_vals import _format_list

        input_val = ['a', 1]

        output = _format_list(input_val)
         
        assert output[1] == 1


    def test_list_dict_value(self):
        from outlib.lib.format_vals import _format_list

        input_val = ['a', {'b': 'c'}]

        output = _format_list(input_val)
         
        assert output[1]['b'] == 'c'


    def test_list_list_value(self):
        from outlib.lib.format_vals import _format_list

        input_val = ['a', ['b', 'c']]

        output = _format_list(input_val)
         
        assert output[1][0] == 'b'


    def test_list_object_value(self):
        from outlib.lib.format_vals import _format_list

        input_val = ['a', TObject(test1='value1')]

        output = _format_list(input_val)
         
        assert output[1]['test1'] == 'value1'


    def test_list_row_proxy_value(self):
        from outlib.lib.format_vals import _format_list

        input_val = ['a', RowProxy(test1='value2')]

        output = _format_list(input_val)
         
        assert output[1]['test1'] == 'value2'



class TestFormatObject(unittest.TestCase):

    def test_object_simple(self):
        from outlib.lib.format_vals import _format_object

        input_val = TObject(a='b')

        output = _format_object(input_val)
         
        assert output['a'] == 'b'


    def test_object_int_value(self):
        from outlib.lib.format_vals import _format_object

        input_val = TObject(a=1)

        output = _format_object(input_val)
         
        assert output['a'] == 1


    def test_object_dict_value(self):
        from outlib.lib.format_vals import _format_object

        input_val = TObject(a={'b': 'c'})

        output = _format_object(input_val)
         
        assert output['a']['b'] == 'c'


    def test_object_list_value(self):
        from outlib.lib.format_vals import _format_object

        input_val = TObject(a=['b', 'c'])

        output = _format_object(input_val)
         
        assert output['a'][0] == 'b'


    def test_object_object_value(self):
        from outlib.lib.format_vals import _format_object

        input_val = TObject(a=TObject(test1='value1'))

        output = _format_object(input_val)
         
        assert output['a']['test1'] == 'value1'


    def test_object_row_proxy_value(self):
        from outlib.lib.format_vals import _format_object

        input_val = TObject(a=RowProxy(test1='value2'))

        output = _format_object(input_val)
         
        assert output['a']['test1'] == 'value2'



class TestFormatRowProxy(unittest.TestCase):

    def test_row_proxy_simple(self):
        from outlib.lib.format_vals import _format_row_proxy

        input_val = RowProxy(a='b')

        output = _format_row_proxy(input_val)
         
        assert output['a'] == 'b'


    def test_row_proxy_int_value(self):
        from outlib.lib.format_vals import _format_row_proxy

        input_val = RowProxy(a=1)

        output = _format_row_proxy(input_val)
         
        assert output['a'] == 1



class TestFormatValue(unittest.TestCase):

    def test_value_string_value(self):
        from outlib.lib.format_vals import format_value

        input_val = 'b'

        output = format_value(input_val)
         
        assert output == 'b'


    def test_value_int_value(self):
        from outlib.lib.format_vals import format_value

        input_val = 1

        output = format_value(input_val)
         
        assert output == 1


    def test_value_dict_value(self):
        from outlib.lib.format_vals import format_value

        input_val = {'b': 'c'}

        output = format_value(input_val)
         
        assert output['b'] == 'c'


    def test_value_list_value(self):
        from outlib.lib.format_vals import format_value

        input_val = ['b', 'c']

        output = format_value(input_val)
         
        assert output[1] == 'c'


    def test_value_object_value(self):
        from outlib.lib.format_vals import format_value

        input_val = TObject(test1='value1')

        output = format_value(input_val)
         
        assert output['test1'] == 'value1'


    def test_value_row_proxy_value(self):
        from outlib.lib.format_vals import format_value

        input_val = RowProxy(test1='value2')

        output = format_value(input_val)
         
        assert output['test1'] == 'value2'
