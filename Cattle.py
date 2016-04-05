import random
import itertools

class Cattle:

	def __init__(self, x, y, x_min, x_max, y_min, y_max):
		self.age = 0;
		self.weight = random.randint(60, 100);
		self.state = 0;
		self.location = 0;
		"""
		0 - farm_random; 1 - farm_traveling; 2 - road;
		3 - sale_barn_1; 4 - stocker;
		5 - sale_barn_2; 6 - feed_lot; 7 - abattoir
		"""
		self.x = x;
		self.y = y;
		self.x_min = x_min;
		self.x_max = x_max;
		self.y_min = y_min;
		self.y_max = y_max;
		self.daysSick =  0;
		self.time1InSale = random.random()*4+1;
		self.time2InSale = random.random()*4+1;

	def infect(self):
		self.state = self.state + 1;

	def recover(self):
		self.state = self.state + 1;

	def move(grid):
		if self.location == 0: #Farm_random
			new_x, new_y = self.random_walk(self.x, self.y);
			if (new_x>self.x_min and new_x<self.x_max and new_y>self.y_min and new_y<self.y_max):	#Check Limits
				if len(grid[new_x, new_y])==0:
					grid[self.x, self.y].remove(self.cattleId);
					self.x = new_x;
					self.y = new_y;
					grid[self.x, self.y].append(self.cattleId);

		if self.location == 1:	#Farm_traveling
			if self.y == y_max:
				location = 2;
			self.y = self.y + 1;

		if self.location == 2:	#Road
			if self.x<50:
				self.x = self.x + 1;
			elif self>52:
				self.x = self.x - 1;
			else
				self.y = self.y + 1;
				location = 3;

		if self.location == 3:	#Sale_barn_1


		if self.location == 4:	#Stocker

			
		if self.location == 5:	#Sale_barn_2

			
		if self.location == 6:	#Feed_lot

			
		if self.location == 7:	#Abettoir

	def increase_weight():
		incr = 0;
		if self.location = 0:
			incr = random.random()*0.25 + 0.5;
		elif self.location = 4;
			incr = random.random()*0.2 + 0.4;
		elif self.location = 6;
			incr = random.random()*0.5 + 0.5;
		self.weight = self.weight + incr;

	def random_walk(self, x, y):
		new_x = x;
		new_y = y;
		walk_rand = random.random();

		if(walk_rand < 0.125):
			new_x = x - 1;
			new_y = y - 1;
		elif(walk_rand < 0.25):
			new_x = x;
			new_y = y - 1;
		elif(walk_rand < 0.375):
			new_x = x + 1;
			new_y = y - 1;
		elif(walk_rand < 0.5):
			new_x = x - 1;
			new_y = y;
		elif(walk_rand < 0.625):
			new_x = x + 1;
			new_y = y;
		elif(walk_rand < 0.75):
			new_x = x - 1;
			new_y = y + 1;
		elif(walk_rand < 0.875):
			new_x = x;
			new_y = y + 1;
		else:
			new_x = x + 1;
			new_y = y + 1;
		return new_x, new_y;