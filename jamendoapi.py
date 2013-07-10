#!/usr/bin/env python

import requests


class jamendo(object):

    def __init__(self, client_id, api_defaults={}, file_defaults={}):

        self.base_url = "http://api.jamendo.com"
        self.api_version = "v3.0"
        self.api_url = "%s/%s" % (self.base_url, self.api_version)
        self.file_endpoint = "tracks/file"

        self.default_api_payload = dict(
            [("client_id", client_id), ("format", "json")] +
            api_defaults.items()
        )

        self.default_file_payload = dict(
            [("client_id", client_id), ("audioformat", "ogg")] +
            file_defaults.items()
        )

    def get(self, data_type, args={}):
        url = "%s/%s" % (self.api_url, data_type)
        payload = dict(
            self.default_api_payload.items() +
            args.items()
        )
        r = requests.get(url, params=payload)
        return r.json()["results"]

    def download_track(self, track_id, args={}):
        url = "%s/%s" % (self.url, self.file_endpoint)
        payload = dict(
            self.default_file_payload.items() +
            args.items() +
            [("id", track_id)]
        )
        r = requests.get(url, params=payload)
        return r


if __name__ == '__main__':
    import unittest
    from tests.testjamendoapi import Testjamendo
    Testjamendo.header()
    unittest.main()
