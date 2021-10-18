#!/usr/bin/python3
#coding: utf-8
__VERSION__ = "0.1.2"

import argparse 
parser = argparse.ArgumentParser("dataMining.py (v{version})\n-------------\ndataMining.py is an program I have write to do an exemple code of the popular concept in crypto-monetic (for an neophyte, yeah just cryptomoney is a lot of things and that just one little piece of the complex innovation of internet.).\n\nMade just for fun and to explain this concept to an nurse.\n...And now I fix this and made preparation to use for and little more biggest project...(Probably an library to the pipy deposit of python3 library's you know...".format(
    version = __VERSION__
    ))

parser.add_argument("-s", "--size", type=int, 
        help="size of valid block repetitions")
parser.add_argument("-q", "--quiet", action="store_true", 
        help="no verbosity")
parser.add_argument("-H" ,"--set-hash-function", type=str,
        default="sha512",
        help="set the algorithm of hash function (used from hashlib).") 
parser.add_argument("filepath", type=str, help="json output file.")
parser.add_argument("data", type=str, required=False, help="data to mine.")
args = parser.parse_args()

if args.size:
    size_=args.size
else:
    size_=4

import os
import hashlib
import base64
from multiprocessing import Process, Pool
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
    def __init__(self,hash_function,size_block_validation=4):
        self.salt = exhaustivitatatator()
        self.hash_function = hash_function
        self.size_block_validation = size_block_validation
    def mining(self,tries=1000000,chrepet="0"):
        for i in range(0,tries):
            self.salt.next()
            if self.hashfunc()[:self.size_block_validation] == chrepet * self.size_block_validation:
                return { "value": self.hashfunc()[self.size_block_validation:], "size_valide_block": self.size_block_validation, "chrepet":chrepet, "iterations": i } 
    def setDataFromArg(self,data):
        self.data = data
    def setDataFromFile(self,filepath):
        with open(filepath, 'rb') as f:
            self.data = f.read().decode()
            f.close()
    def setDataFromFileWithSaltedArg(self,filepath,data):
        self.setDataFromFile(filepath)
        self.data = self.data + data
    def hashfunc(self):
        hashlib.new(self.hash_function)
        hashlib.update("".join(self.salt.get()+list(self.data)).encode())
        return hashlib.hexdigest()

def callErrorShowFunction(TYPE_ERR_DESC):
    print("Error: {typeErr}".format(
        typeErr = TYPE_ERR_DESC
        ))
    exit(-1)


# =====================
dm = dataMiner(args.set_hash_function,size_)
if (args.filepath) and (args.data):
    dm.setDataFromFileWithSaltedArg(args.filepath, args.data)
elif args.filepath:
    dm.setDataFromFile(args.filepath)
elif args.data:
    dm.setDataFromArg(args.data)
else:
    dm.callErrorShowFunction("NULL DATA FROM INPUT")

informations=dm.mining()
with open(args.filepath,'w+b') as f:
    f.write(json.dumps(informations,indent=4).encode())
    f.close()
if not args.quiet:
    print ("\n\n\nvalue: {}\niterations: {}\nsize_block_validation: {}\ncharacter_repeted: {}".format(informations["value"],informations["iterations"],informations["size_valide_block"],informations["chrepet"]))


