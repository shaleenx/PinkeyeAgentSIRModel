from Cattle import Cattle
from Farm import Farm
from SaleBarn import SaleBarn
from Stocker import Stocker
from Feedlot import Feedlot
import random

################# Inital Constant #################

cInitProb = 0.1
gridHeight = 126
gridWidth = 100
numberFarm = 6
dt = 0.25
currentTime = 0
infPeriod = 40
infProb = 1

numS = [0]
numI = [0]
numR = [0]
cumI = [0]
numC = [0]

################# Inital Constant #################
ucl = []
gridList = [[[] for x in range(gridWidth)] for x in range(gridHeight)] 
farmList = []

for i in range(numberFarm):
	farmList.append(Farm(16*i + i, 0, 16*(i+1) + i + 1, 95, cInitProb))
	farmList.initializeCattle(ucl,gridList)

numS[0] = len(ucl) - 1
numI[0] = 1
numC[0] = len(ucl)
cumI[0] = 1

stocker = Stocker(0, 96, 49, 125)
saleBarn = SaleBarn(50, 96, 52, 125)
feedlot = Feedlot(53, 96, 72, 125)

def analyseGrid():
	for i in range(len(ucl)) and ucl[i].location != 8:
		if ucl[i].state == 0:
			for j in range(-1,2):
				for k in range(-1,2):
					if ucl[i].x + j >= ucl[i].x_min and ucl[i].x + j <= ucl[i].x_max and ucl[i].y + k >= ucl[i].y_min and ucl[i].y + k <= ucl[i].y_max:
						for l in gridList[ucl[i].x + j][ucl[i].y + k]:
							if ucl[l].state == 1 and ucl[i].location != 8:
								if random.random() < infProb:
									ucl[i].state = ucl[i].state + 1
									numS.append(numS[len(numS)-1] - 1)
									numI.append(numI[len(numI)-1] + 1)
									cumI.append(cumI[len(cumI)-1] + 1)
									break
					if ucl[i].state == 1:
						break

while True:
	currentTime = currentTime + dt
	numC.append(len(ucl))
	analyseGrid()
	numR.append(numR[len(numR)-1])

	for i in range(len(ucl)):
		ucl[i].move(gridList)
		ucl[i].increase_weight()
		
		if ucl[i].state == 1:
			ucl[i].daysSick = ucl[i].daysSick + dt
			if ucl[i].daysSick == infPeriod:
				ucl[i].state = ucl[i].state + 1;
				numI[len(numI)-1] = numI[len(numI)-1] - 1
				numR[len(numR)-1] = numR[len(numR)-1] - 1
		
		if ucl[i].location == 8:
			numC[len(numC) - 1] = numC[len(numC) - 1] - 1
	if numC[len(numC) - 1]==0:
		break