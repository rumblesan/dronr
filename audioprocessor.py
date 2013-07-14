#!/usr/bin/env python

import subprocess


class AudioProcessor(object):

    def __init__(self,
                 decoder='ffmpeg',
                 encoder='ffmpeg',
                 stretcher='wavstretch',
                 encoderOpts=None,
                 stretcherOpts=None):

        self.decoder = decoder
        self.encoder = encoder
        self.stretcher = stretcher

        if encoderOpts:
            self.encoderOpts = encoderOpts
        else:
            self.encoderOpts = []

        if encoderOpts:
            self.stretcherOpts = stretcherOpts
        else:
            self.stretcherOpts = []

    def encode(self, inputfile, outputfile):
        command = [self.encoder] + self.encoderOpts
        subprocess.call(command + ["-i", inputfile, outputfile])
        subprocess.call(["rm", inputfile])

    def decode(self, inputfile, outputfile):
        subprocess.call([self.decoder, "-i", inputfile, outputfile])
        subprocess.call(["rm", inputfile])

    def stretch(self, inputfile, outputfile):
        command = [self.stretcher] + self.stretcherOpts
        fileargs = ["-i", inputfile, "-o", outputfile]
        subprocess.call(command + fileargs)
        subprocess.call(["rm", inputfile])


if __name__ == '__main__':
    import unittest
    from tests.testaudioprocessor import TestAudioProcessor
    TestAudioProcessor.header()
    unittest.main()
