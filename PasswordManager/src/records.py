#!/usr/bin/env python

class Data :
	def __init__(self, account, usr, pwd) :
		self.id = account	
		self.username = usr
		self.password = pwd
		self.moreInfo = []
	
	def addMoreDetails(self, moreInfo) :
		self.moreInfo.append(moreInfo)
	
	def printMe(self) : 
		print "-------- Your "+self.id + " details --------"
		print "username : " + self.username
		print "password : " + self.password
		print "details  : " + str(self.moreInfo)		

