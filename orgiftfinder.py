#!/usr/bin/env python

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/orgiftfinder', methods=['POST'])
def ordemoapp2():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") != "findGift":
        return {}

    result = req.get("result")
    parameters = result.get("parameters")
    subclass = parameters.get("subclass")
    if subclass is None:
        return {}

    res = makeResult(subclass)
    return res


def makeResult(subclass):
    print(subclass)
    if len(subclass) == 0:
        return {
            "speech": "No result found",
            "displayText": "No result found",
            "source": "orgiftfinder"
            }

    #data = json.dumps(subclass)
	
    data = {'basicCard' : {'title': 'title', 'formattedText': 'formatted title.', 'image': {'url': 'https://www.google.com/search?q=jeans','accessibilityText': 'Image text'}}}
	
    speech = "First few results are as follows"

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
		"data": data,
        "source": "ordemoapp2"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
