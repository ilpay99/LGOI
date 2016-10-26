class Glob(object):
	"""This is a place to save some important data"""

	def sendUserMessage(self,Username,Password):
		self._Password=Password
		self._Username=Username
	def sendAccessResult(self,AccessResult):
		self._AccessResult=AccessResult
	def getAccessResult(self):
		return self._AccessResult
	def __init__(self):
		self._Password=None
		self._Username=None
		self._AccessResult=-1
		pass
_Glob=Glob()