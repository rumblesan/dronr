#!/usr/bin/env python

import unittest
from jamendoapi import jamendo


class Testjamendo(unittest.TestCase):

    @staticmethod
    def header():
        print("\n")
        print("*************************************")
        print("    Running tests on jamendo")
        print("*************************************")
        print("\n")

    def test_creation(self):
        j = jamendo("somefakeid")
        self.assertIsInstance(j, jamendo)
