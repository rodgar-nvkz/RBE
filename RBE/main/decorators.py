__author__ = 'rd'
from django.http import HttpResponse
from django.utils import simplejson


def json_response(view):
    def wrap(request, *args, **kwargs):
        res = view(request, *args, **kwargs)
        if res is None:
            res = {'error': 'no data'}
        if isinstance(res, (dict, list)):
            return HttpResponse(simplejson.dumps(res, ensure_ascii=False, encoding='utf-8'),
                                mimetype='application/json')
        return res
    wrap.__doc__ = view.__doc__
    wrap.__name__ = view.__name__
    return wrap


def http_response(view):
    def wrap(request, *args, **kwargs):
        res = view(request, *args, **kwargs)
        if res is None:
            res = u'empty response'
        if isinstance(res, (unicode, str)):
            return HttpResponse(res)
        if isinstance(res, (dict, list)):
            return HttpResponse(simplejson.dumps(u"object: %s" % res, ensure_ascii=False, encoding='utf-8'),
                                mimetype='text/plain')
        return res
    wrap.__doc__ = view.__doc__
    wrap.__name__ = view.__name__
    return wrap