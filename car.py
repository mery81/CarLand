#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CarLand Final Project"""

import vehicle


class car(vehicle.vehicle):
    def __init__(self, serielno, fuel, modelyear, color, manufacture, model,
                 type):
        #super(self.__class__, self).__init__('car', serielno, fuel, type)
        vehicle.vehicle.__init__(self, 'car', serielno, fuel, type)
        self.modelyear = modelyear
        self.color = color
        self.manufacture = manufacture
        self.model = model

    def getModelYear(self):
        """Fetches the car model year from inventory"""
        return self.modelyear

    def getColor(self):
        """Fetches the car color from inventory"""
        return self.color

    def getManufature(self):
        """Fetches the car manufacture from inventory"""
        return self.manufacture

    def getModel(self):
        """Fetches the car model from inventory"""
        return self.model
