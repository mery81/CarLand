#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CarLand Final Project"""

class vehicle(object):
    def __init__(self, type, serielno, fuel, old_new):
        self.type = type
        self.fuel = fuel
        self.old_new = old_new
        self.serielno = serielno

    def getType(self):
        return self.type

    def getFuel(self):
        return self.fuel

    def getSerielno(self):
        return self.serielno
