import random
from limits import universe


class Cattle:

	def __init__(self, cattleId, x, y, x_min, x_max, y_min, y_max):
		self.age = 0
		self.weight = random.randint(60, 100)
		self.state = 0
		self.location = 0
		self.cattleId = cattleId
		"""
		0 - farm_random; 1 - farm_traveling; 2 - road;
		3 - sale_barn_1; 4 - stocker_random; 5 - stocker_traveling
		6 - sale_barn_2; 7 - feed_lot; 8 - abattoir
		"""
		self.x = x
		self.y = y
		self.x_min = x_min
		self.x_max = x_max
		self.y_min = y_min
		self.y_max = y_max
		self.daysSick = 0
		self.time1InSale = random.random() * 4 + 1
		self.time2InSale = random.random() * 4 + 1

	def move(self, grid):
		if self.location == 0:  # Farm_random
			new_x, new_y = self.random_walk(self.x, self.y)
			# Check Limits
			if (new_x >= self.x_min and new_x <= self.x_max and new_y >= self.y_min and new_y <= self.y_max):
				if len(grid[new_x][new_y]) == 0:
					grid[self.x][self.y].remove(self.cattleId)
					self.x = new_x
					self.y = new_y
					grid[self.x][self.y].append(self.cattleId)

		elif self.location == 1:  # Farm_traveling
			if self.y == self.y_max:
				self.location = 2
			grid[self.x][self.y].remove(self.cattleId)
			self.y = self.y + 1
			grid[self.x][self.y].append(self.cattleId)

		elif self.location == 2:  # Road
			if self.x < universe['salebarn']['minX']:
				grid[self.x][self.y].remove(self.cattleId)
				self.x = self.x + 1
				grid[self.x][self.y].append(self.cattleId)
			elif self > universe['salebarn']['maxX']:
				grid[self.x][self.y].remove(self.cattleId)
				self.x = self.x - 1
				grid[self.x][self.y].append(self.cattleId)
			else:
				grid[self.x][self.y].remove(self.cattleId)
				self.y = self.y + 1
				grid[self.x][self.y].append(self.cattleId)
				self.location = 3
				self.x_min = universe['salebarn']['minX']
				self.x_max = universe['salebarn']['maxX']
				self.y_min = universe['salebarn']['minY']
				self.y_max = universe['salebarn']['maxY']

		elif self.location == 3:  # Sale_barn_1
			new_x, new_y = self.random_walk(self.x, self.y)
			# Check Limits
			if (new_x >= self.x_min and new_x <= self.x_max and new_y >= self.y_min and new_y <= self.y_max):
				grid[self.x][self.y].remove(self.cattleId)
				self.x = new_x
				self.y = new_y
				grid[self.x][self.y].append(self.cattleId)

		elif self.location == 4:  # Stocker_random
			new_x, new_y = self.random_walk(self.x, self.y)
			# Check Limits
			if (new_x >= self.x_min and new_x <= self.x_max and new_y >= self.y_min and new_y <= self.y_max):
				if len(grid[new_x][new_y]) == 0:
					grid[self.x][self.y].remove(self.cattleId)
					self.x = new_x
					self.y = new_y
					grid[self.x][self.y].append(self.cattleId)

		elif self.location == 5:  # Stocker_traveling
			if self.x == self.x_max:
				self.location = 6
			grid[self.x][self.y].remove(self.cattleId)
			self.x = self.x + 1
			grid[self.x][self.y].append(self.cattleId)

		elif self.location == 6:  # Sale_barn_2
			new_x, new_y = self.random_walk(self.x, self.y)
			# Check Limits
			if (new_x >= self.x_min and new_x <= self.x_max and new_y >= self.y_min and new_y <= self.y_max):
				grid[self.x][self.y].remove(self.cattleId)
				self.x = new_x
				self.y = new_y
				grid[self.x][self.y].append(self.cattleId)

		elif self.location == 7:  # Feed_lot
			new_x = x + 1
			if (new_x <= self.x_max):
				if len(grid[new_x, new_y]) == 0:
					grid[self.x][self.y].remove(self.cattleId)
					self.x = new_x
					grid[self.x][self.y].append(self.cattleId)

	def increase_weight(self):
		incr = 0
		if self.location == 0:
			incr = random.random() * 0.25 + 0.5
		elif self.location == 4:
			incr = random.random() * 0.2 + 0.4
		elif self.location == 7:
			incr = random.random() * 0.5 + 0.5
		self.weight = self.weight + incr

		if self.location == 0 and self.weight > 600:
			self.location = 1

		if self.location == 4 and self.weight > 900:
			self.location = 5

		if self.location == 7 and self.weight > 1300 and self.x == self.x_max:
			self.location = 8

	def random_walk(self, x, y):
		new_x = x
		new_y = y
		walk_rand = random.random()

		if(walk_rand < 0.125):
			new_x = x - 1
			new_y = y - 1
		elif(walk_rand < 0.25):
			new_x = x
			new_y = y - 1
		elif(walk_rand < 0.375):
			new_x = x + 1
			new_y = y - 1
		elif(walk_rand < 0.5):
			new_x = x - 1
			new_y = y
		elif(walk_rand < 0.625):
			new_x = x + 1
			new_y = y
		elif(walk_rand < 0.75):
			new_x = x - 1
			new_y = y + 1
		elif(walk_rand < 0.875):
			new_x = x
			new_y = y + 1
		else:
			new_x = x + 1
			new_y = y + 1
		return new_x, new_y
