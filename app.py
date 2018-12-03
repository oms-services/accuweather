# -*- coding: utf-8 -*-
import json
import os
import sys

import requests

from flask import Flask, make_response, request


class Handler:
    app = Flask(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.api_key = os.getenv('API_KEY')

    def forecast(self):
        req = request.get_json()
        location = req['location']
        res = requests.get(f'https://dataservice.accuweather.com'
                           f'/locations/v1/cities/search',
                           params={
                               'apikey': self.api_key,
                               'q': location
                           })
        if res.status_code != 200:
            return self.end({
                'success': False,
                'error': f'AccuWeather responded with a {res.status_code}!'
            })

        json_res = res.json()
        if len(json_res) == 0:
            return self.end({
                'success': False,
                'error': f'Location not found!'
            })

        key = json_res[0]['Key']

        res = requests.get(f'https://dataservice.accuweather.com'
                           f'/currentconditions/v1/{key}',
                           params={
                               'apikey': self.api_key,
                               'details': True
                           })

        if res.status_code != 200:
            return self.end({
                'success': False,
                'error': f'AccuWeather responded with a {res.status_code}!'
            })

        json_res = res.json()
        out = json_res[0]
        out['success'] = True
        return self.end(out)

    @staticmethod
    def end(res):
        resp = make_response(json.dumps(res))
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp


if __name__ == '__main__':
    if os.getenv('API_KEY') is None:
        print('Environment variable API_KEY not found.')
        sys.exit(1)

    handler = Handler()
    handler.app.add_url_rule('/forecast', 'forecast', handler.forecast,
                             methods=['post'])
    handler.app.run(host='0.0.0.0', port=8000)
