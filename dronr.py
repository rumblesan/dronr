#! /usr/bin/env python

import ConfigParser
import argparse
from datetime import datetime

from jamendoapi import jamendo

import random


def parseArgs():
    parser = argparse.ArgumentParser(description='Stretch track for Tumblr')
    parser.add_argument('config', help='The config file')
    args = parser.parse_args()

    config = ConfigParser.SafeConfigParser()
    config.read(args.config)

    return (args, config)


def main():

    print('###################')
    print('#      Dronr      #')
    print('###################')
    print('\n')
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    args, config = parseArgs()
    #consumerKey = config.get('consumer', 'key')
    #consumerSecret = config.get('consumer', 'secret')
    #oauthToken = config.get('oauth', 'key')
    #oauthSecret = config.get('oauth', 'secret')

    jamendo_client_id = config.get('jamendo', 'clientid')

    track_ordering = config.get('jamendo', 'track_ordering')
    audio_format = config.get('audio', 'format')

    j = jamendo(jamendo_client_id)

    top100_args = {
        "limit": 100,
        "order": track_ordering,
        "ccsa": 1
    }
    top100 = j.get("tracks", top100_args)

    track = random.choice(top100)

    print(track)

    download_track(j, track["id"], track["name"], audio_format)


def download_track(jamendo, track_id, track_name, file_format):

    print("Downloading %s" % track_name)
    dl_request_args = {
        "audioformat": file_format
    }

    filename = track_name.lower().replace(' ', '_') + "." + file_format

    with open(filename, "w") as fp:
        raw_response = jamendo.download_track(track_id, dl_request_args)
        fp.write(raw_response.read())


if __name__ == "__main__":
    main()
