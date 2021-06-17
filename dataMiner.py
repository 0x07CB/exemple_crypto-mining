#!/usr/bin/python3
import os
import hashlib
import base64
from multiprocessing import Process, Pool
import argparse

possible_characts = range(0,255)

class exhaustivitatatator(object):
    def __init__(self,size=64):
        self.size = size
        self.init()
    def next(self):
        pass
    def init(self):
        self.value = chr(0) * self.size
    def get(self):
        return self.value
    
class dataMiner(object):
    def __init__(self):
        self.data = exhaustivitatatator()
    def mining(self):
        pass
    def set_data(self):
        pass
    def hashfunc(self,salt):
        hashlib.sha3_256(self.data.value,salt).hexdigest()


