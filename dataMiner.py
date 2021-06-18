#!/usr/bin/python3
import os
import hashlib
import base64
from multiprocessing import Process, Pool
import argparse
import json
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
                return { "value": self.hashfunc()[self.size_block_validation:], "size_valide_block": self.size_block_validation, "chrepet":chrepet, "iterations": i } 
    def set_data(self,data):
        self.data = data
    def hashfunc(self):
        return hashlib.sha3_256("".join(self.salt.get()+list(self.data)).encode()).hexdigest()



parser = argparse.ArgumentParser()
parser.add_argument("-s","--size",type=int, help="size of valid block repetitions")
parser.add_argument("-q","--quiet",action="store_true", help="no verbosity")
parser.add_argument("filepath", help="json output file")
parser.add_argument("data", help="data to mine")
args = parser.parse_args()

if args.size:
    size_=args.size
else:
    size_=4
dm = dataMiner(size_)
dm.set_data(args.data)
informations=dm.mining()
with open(args.filepath,'w+b') as f:
    f.write(json.dumps(informations,indent=4).encode())
    f.close()
if not quiet:
    print ("\n\n\nvalue: {}\niterations: {}\nsize_block_validation: {}\ncharacter_repeted: {}".format(informations["value"],informations["iterations"],informations["size_valide_block"],informations["chrepet"]))


