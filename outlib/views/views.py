from pyramid.view import view_config
from outlib.lib.wout import output_to_logger, value_to_json
from outlib.lib.format_vals import format_value


@view_config(route_name='home', renderer='json')
def my_view(request):
    output_to_logger(format_value({'a': 'b'}))
    output_to_logger(value_to_json(format_value({'c': ['d', 1]})))
    return {'project': 'outlib'}
