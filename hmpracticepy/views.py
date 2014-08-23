__author__ = 'scottumsted'
from flask import json, request
from hmpracticepy import app
from data import models


def _padded_jsonify(callback, *args, **kwargs):
    content = str(callback) + '(' + json.dumps(dict(*args, **kwargs)) + ')'
    return app.response_class(content, mimetype='application/json')


def _regular_jsonify(o):
    content = json.dumps(o)
    return app.response_class(content, mimetype='application/json')


@app.route('/source.json/', methods=['GET', 'POST'])
def latest_json():
    result = []
    callback = request.args.get('callback', None)
    try:
        sources = models.Models.get_sources()
        if sources is not None:
            result = sources
    except Exception, e:
        result = []
    if callback is None:
        result = _regular_jsonify(result)
    else:
        result = _padded_jsonify(callback, result)
    return result
