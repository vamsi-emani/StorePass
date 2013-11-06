#!/usr/bin/python

import utils
from manager import Manager
from records import Data

mgr = utils.deserializeManagerFromDisk()

print(" ***** Welcome to password manager *****\n")
print(">> What do you want to do?")
print("1. Add account details")
print("2. Edit existing account details")
print("3. Delete all existing account details")
print("4. View all account details")
print("5. View existing account details\n")

actionInput = raw_input(">> Enter the option number to tell me what you want me to do ?")


if actionInput == "1" :
	mgr.enter()	
	utils.serializeManagerToDisk(mgr)
        print "Account added"
    
elif actionInput == "2" :
	mgr.edit()
	utils.serializeManagerToDisk(mgr)
        print "Account edited"

elif actionInput == "3" :
	mgr.destroy()
	utils.serializeManagerToDisk(mgr)
        print "Accounts destroyed"

elif actionInput == "4" :
	mgr.printAll()
        
elif actionInput == "5" :       
       mgr.find(raw_input(">> Enter account name : ")).printMe()
       
else :
	data = mgr.find(sys.argv[1])
	data.printMe()




