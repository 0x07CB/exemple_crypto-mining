#!/usr/bin/python3
import os
import hashlib
import base64
from multiprocessing import Process, Pool
import argparse

class exhaustivitatatator(object):
    def __init__(self,size=64):
        self.size = size
        self.init()
    def next(self):
        self.value[0] = chr((int(ord(self.value[0]))+1)%256)
        for i in range
    def init(self):
        self.value = chr(0) * self.size
    def get(self):
        return self.value
    
class dataMiner(object):
    def __init__(self):
        self.data = exhaustivitatatator()
    def mining(self):
        d
    def set_data(self,data):
        self.data = data
    def hashfunc(self,salt):
        hashlib.sha3_256(self.data.value,salt).hexdigest()


