class Feedlot:
	''' Class for Feedlot area '''
	def __init__(self, minX, minY, maxX, maxY):
		self.minX = minX
		self.minY = minY
		self.maxX = maxX
		self.maxY = maxY
		self.height  = maxY - minY
		self.width = maxX - minX

	def getMinX(self):
		return self.minX

	def getMinY(self):
		return self.minY

	def getMaxX(self):
		return self.maxX

	def getMaxY(self):
		return self.maxY