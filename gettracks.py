#! /usr/bin/env python

import json
import urllib


def main():
    top100 = getTop100()

    first = top100[0]
    downloadTrack(first["id"], first["name"])


def getTop100():
    jamendoApi = "http://api.jamendo.com/en/get2/id+name/track/json/"
    topArgs = {"n": 100, "order": "ratingday_desc"}
    top100Url = jamendoApi + "?" + urllib.urlencode(topArgs)

    print("Getting top 100 tracks for today")

    result = json.load(urllib.urlopen(top100Url))
    return result


def downloadTrack(trackId, trackName):
    jamendoStorage = "http://storage.newjamendo.com/"
    trackArgs = {"trackid": trackId, "format": "ogg2"}
    trackUrl = jamendoStorage + "?" + urllib.urlencode(trackArgs)

    print("Downloading track")
    print(trackUrl)

    webFile = urllib.urlopen(trackUrl)
    localFile = open(trackName, "w")

    localFile.write(webFile.read())

    webFile.close()
    localFile.close()


if __name__ == "__main__":
    main()
