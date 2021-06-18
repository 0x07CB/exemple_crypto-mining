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
        self.value=list(self.value)
    def next(self):
        self.value[0] = chr(((int(ord(self.value[0]))+1)%256))
        for i in range(0,self.size):
            if self.value[0+i] == chr(0):
                self.value[0+i+1] = chr((int(ord(self.value[0+i+1]))+1)%256)
            else:
                break
    def init(self):
        self.value = chr(0) * self.size
    def get(self):
        return self.value
    
class dataMiner(object):
    def __init__(self,size_block_validation=4):
        self.salt = exhaustivitatatator()
        self.size_block_validation = size_block_validation
    def mining(self,tries=1000000,chrepet="0"):
        for i in range(0,tries):
            self.salt.next()
            if self.hashfunc()[:self.size_block_validation] == chrepet * self.size_block_validation:
                return i
    def set_data(self,data):
        self.data = data
    def hashfunc(self):
        return hashlib.sha3_256("".join(self.salt.get()+list(self.data)).encode()).hexdigest()

dm = dataMiner()

dm.set_data("test blabla")
print (dm.mining())


