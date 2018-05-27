"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request
from flask_restplus import Api

from app.api.rest.base import BaseResource, SecureResource, RadioCommand
from app.api import api_rest

from controlserver import vlc_controller


@api_rest.route('/resource/<string:resource_id>')
class ResourceOne(BaseResource):
    """ Sample Resource Class """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp, 'resource': resource_id}

    def post(self, resource_id):
        json_payload = request.json
        return {'timestamp': json_payload}, 201


@api_rest.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}


@api_rest.route('/radio/play')
class RadioPlay(RadioCommand):

    def get(self):
        play_url = 'http://metafiles.gl-systemhaus.de/hr/hrinfo_2.m3u'
        vlc_controller.add(play_url)
        timestamp = datetime.utcnow().isoformat()
        return {'command': 'add',
                'args': [play_url],
                'timestamp': timestamp}


@api_rest.route('/radio/stop')
class RadioStop(RadioCommand):

    def get(self):
        vlc_controller.stop()
        timestamp = datetime.utcnow().isoformat()
        return {'command': 'stop',
                'args': [],
                'timestamp': timestamp}
