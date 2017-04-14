def wsgi_application (environ, start_response):
    body = [bytes (i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return body