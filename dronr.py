#! /usr/bin/env python

import ConfigParser
import argparse
from datetime import datetime

from jamendoapi import jamendo

from audioprocessor import AudioProcessor

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

    audio = AudioProcessor()

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

    track_name = track["name"].lower().replace(' ', '_')
    track_file = track_name + "." + audio_format

    wave_name = track_name + ".wav"
    stretched_wave = track_name + "-stretched.wav"
    final_file = track_name + "-stretched.mp3"

    download_track(j, track["id"], track_file, audio_format)

    audio.decode(track_file, wave_name)
    audio.stretch(wave_name, stretched_wave)
    audio.encode(stretched_wave, final_file)


def download_track(jamendo, track_id, track_name, file_format):

    print("Downloading %s" % track_name)
    dl_request_args = {
        "audioformat": file_format
    }

    with open(track_name, "w") as fp:
        raw_response = jamendo.download_track(track_id, dl_request_args)
        fp.write(raw_response.read())


if __name__ == "__main__":
    main()
