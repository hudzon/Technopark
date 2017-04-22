from pprint import pformat
from cgi import parse_qsl, escape

def application(environ, start_response):
    result = []

    result.append('<h1>Hello, world!</h1>')
    result.append('<form method="post">')
    result.append('<input type="text" name = "post1">')
    result.append('<input type="text" name = "post2">')
    result.append('<input type="submit" value="Post">')
    result.append('</form>')
    result.append('<form method="get">')
    result.append('<input type="text" name = "get1">')
    result.append('<input type="text" name = "get2">')
    result.append('<input type="submit" value="Get">')
    result.append('</form>')

    if environ['REQUEST_METHOD'] == 'POST':
        if environ['wsgi.input'] != '':
            result.append('<h3>Post data:</h3>')
            data_parse = parse_qsl(environ['wsgi.input'].read())
            for elem in data_parse:
                result.append(' = '.join(elem))
                result.append('1<br>')

    if environ['REQUEST_METHOD'] == 'GET':
        if environ['QUERY_STRING'] != '':
            data_parse = parse_qsl(environ['QUERY_STRING'])
            result.append('<h3>Get data:</h3>')
            for elem in data_parse:
                result.append(' = '.join(elem))
                result.append('<br>')

    result_len = sum(len(line) for line in result)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(result_len))])
    return result
