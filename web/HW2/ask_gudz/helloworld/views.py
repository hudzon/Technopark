from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def hello(request):
    args = {}
    result = []

    result.append('<h1>Hello, world!</h1>')
    #result.append('<form method="post">')
    #result.append('<input type="text" name = "post1">')
    #result.append('<input type="text" name = "post2">')
    #result.append('<input type="submit" value="Post">')
    #result.append('</form>')
    result.append('<form method="get">')
    result.append('<input type="text" name = "get1">')
    result.append('<input type="text" name = "get2">')
    result.append('<input type="submit" value="Get">')
    result.append('</form>')

    #if request.method == 'POST':
    #    result.append('<h3>Post data:</h3>')
    #    for key, value in request.Post.iteritems():
    #        if value != '':
    #            result.append("{} = {}".format(key, value))
    #            result.append('<br>')

    if request.method == 'GET':
        result.append('<h3>Get data:</h3>')
        for key, value in request.GET.iteritems():
            if value != '':
                result.append("{} = {}".format(key, value))
                result.append('<br>')

    return HttpResponse(result)
