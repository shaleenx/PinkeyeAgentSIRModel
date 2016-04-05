from Cattle import Cattle
from random import random


class farm:
	''' Class for farm area '''
	def __init__(self, minX, minY, maxX, maxY, p):
		self.minX = minX
		self.minY = minY
		self.maxX = maxX
		self.maxY = maxY
		self.height = maxY - minY
		self.width = maxX - minX
		self.p = p

	def getMinX(self):
		return self.minX

	def getMinY(self):
		return self.minY

	def getMaxX(self):
		return self.maxX

	def getMaxY(self):
		return self.maxY

	def initializeCattle(self, ucl, grid):
		# Iterate over the grid in the limits of the farm
		for i in range(self.minX, self.maxX+1):
			for j in range(self.minY, self.maxY+1):
				# If probabilistic birth happens,
				if birth(self.p):
					# Create new cattle
					c = Cattle(i, j)
					# Add cattle to Universal Cattle List (UCL)
					ucl.append(c)
					# Place cattle on grid
					grid[i][j].append(len(ucl)-1)


# Utility functions
def birth(p):
	if random() < p:
		return True
	else
		return False
