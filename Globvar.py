import sys
import os
from os.path import *
class Glob(object):
	"""This is a place to save some important data"""
	def PrintToDataText(self,key,value):
		DataText=open(self.DataTextPath,"a")
		if not (key=="" or key==None or key=="\n"):
			if not (value=="" or value==None or value=="\n"):
				DataText.write(key+' '+value+'\n')
	
	def sendUserMessage(self,Username,Password):
		self._dat["Password"]=Password
		self._dat["Username"]=Username
		DataText=open(self.DataTextPath,"a")
		self.PrintToDataText("Password",self._dat["Password"])
		self.PrintToDataText("Username",self._dat["Username"])
	def sendAccessResult(self,AccessResult):
		self._dat["AccessResult"]=AccessResult

	def getAccessResult(self):
		return self._dat["AccessResult"]

	def sendScreenSize(self,width,height):
		self._dat["ScreenHeight"]=height
		self._dat["ScreenWidth"]=width

	def ReadDataText(self):
		if (not exists(self.DataTextPath)):
			write=open(self.DataTextPath,"w")
		DataText=open(self.DataTextPath,"r")
		for nowLine in DataText.readlines():
			data=nowLine.split()
			while len(data)<2:
				data.append(None)
			self._dat[data[0]]=data[1]

	def getdata(self,key):
		return self._dat[key]

	def __init__(self):
		self.DataTextPath=".\\Userdata\\data.dat"
		self._dat={}
		self._dat["Password"]=None
		self._dat["Username"]=None
		self._dat["AccessResult"]=-1
		self.ReadDataText()
		pass
_Glob=Glob()
