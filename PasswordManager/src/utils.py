#!/usr/bin/env python

import pickle
import base64
import subprocess
import os
from manager import Manager

name = 'config'

encFileName = name +'.gpg'

def encrypt():
    subprocess.call(['gpg --yes --batch -c '+name], shell=True)    
    
def decrypt():
    if ( os.path.isfile(encFileName)):
        subprocess.call(['gpg --yes --batch '+encFileName], shell=True)            	

def delete():
    os.remove(name)
    
def serializeManagerToDisk(mgr):    
    with open(name, 'wb') as f:
	pickle.dump(mgr, f)
    encrypt()
    delete()

	
def deserializeManagerFromDisk():    
    try :
        decrypt()
	with open(name, 'rb') as f:
            mgr = pickle.load(f)
        delete()
        return mgr
    except IOError:
        return Manager()
    


