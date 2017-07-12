# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 23:11:37 2017

@author: ASUS
"""

class carData:
    def __init__(self,carName,carPrice):
        self.name = carName
        self.price = carPrice
        
    def __repr__(self):
        return "<%s : %d>" % (self.name, self.price)
    
    def __str__(self):
        return self.name + ": " + str(self.price)