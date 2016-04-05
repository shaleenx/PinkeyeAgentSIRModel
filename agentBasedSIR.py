from Farm import Farm
from SaleBarn import SaleBarn
from Stocker import Stocker
from Feedlot import Feedlot
import random

# ================= Inital Constant ===================

cInitProb = 0.1
gridHeight = 126
gridWidth = 101
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

# ================= Inital Constant ===================
ucl = []
gridList = [[[] for x in range(gridHeight)] for x in range(gridWidth)]
farmList = []

for i in range(numberFarm):
	farmList.append(Farm(16 * i + i, 0, 16 * (i + 1) + i - 1, 94, cInitProb))
	farmList[i].initializeCattle(ucl, gridList)

numS[0] = len(ucl) - 1
numI[0] = 1
numC[0] = len(ucl)
cumI[0] = 1

stocker = Stocker(0, 96, 49, 125)
saleBarn = SaleBarn(50, 96, 52, 125)
feedlot = Feedlot(53, 96, 72, 125)


def analyseGrid():
	for i in range(len(ucl)):

		if ucl[i].state == 0 and ucl[i].location != 8:
			for j in range(-1, 2):
				for k in range(-1, 2):
					if ucl[i].x + j >= ucl[i].x_min and ucl[i].x + j <= ucl[i].x_max and ucl[i].y + k >= ucl[i].y_min and ucl[i].y + k <= ucl[i].y_max:
						# print("["+str(ucl[i].x+j)+", "+str(ucl[i].y+k)+"]")
						if len(gridList[ucl[i].x + j][ucl[i].y + k]) is not 0:
							for l in gridList[ucl[i].x + j][ucl[i].y + k]:
								if ucl[l].state == 1 and ucl[i].location != 8:
									if random.random() < infProb:
										ucl[i].state = ucl[i].state + 1
										numS[len(numS) - 1] = numS[len(numS) - 1] - 1
										numI[len(numI) - 1] = numI[len(numI) - 1] + 1
										cumI[len(cumI) - 1] = cumI[len(cumI) - 1] + 1
										break
					if ucl[i].state == 1:
						break

while True:
	currentTime = currentTime + dt
	
	numS.append(numS[len(numS) - 1])
	numI.append(numI[len(numI) - 1])
	numR.append(numR[len(numR) - 1])
	cumI.append(cumI[len(cumI) - 1])
	numC.append(len(ucl))

	analyseGrid()

	for i in range(len(ucl)):
		ucl[i].move(gridList)
		ucl[i].increase_weight()

		if ucl[i].state == 1:
			ucl[i].daysSick = ucl[i].daysSick + dt
			if ucl[i].daysSick == infPeriod:
				ucl[i].state = ucl[i].state + 1
				numI[len(numI) - 1] = numI[len(numI) - 1] - 1
				numR[len(numR) - 1] = numR[len(numR) - 1] - 1

		if ucl[i].location == 3:
			ucl[i].time1InSale = ucl[i].time1InSale - dt
			if ucl[i].time1InSale <= 0:
				gridList[ucl[i].x][ucl[i].y].remove(ucl[i].cattleId)
				ucl[i].location = ucl[i].location + 1
				ucl[i].x_min = 0
				ucl[i].x_max = 49
				ucl[i].y_min = 96
				ucl[i].y_max = 125
				ucl[i].x = int(random.random() * 49 + 1)
				ucl[i].y = int(96 + random.random() * 30)
				gridList[ucl[i].x][ucl[i].y].append(ucl[i].cattleId)

		if ucl[i].location == 6:
			ucl[i].time2InSale = ucl[i].time2InSale - dt
			if ucl[i].time2InSale <= 0:
				gridList[ucl[i].x][ucl[i].y].remove(ucl[i].cattleId)
				ucl[i].location = ucl[i].location + 1
				ucl[i].x_min = 53
				ucl[i].x_max = 72
				ucl[i].y_min = 96
				ucl[i].y_max = 125
				ucl[i].x = ucl[i].x_min
				gridList[ucl[i].x][ucl[i].y].append(ucl[i].cattleId)

		if ucl[i].location == 8:
			numC[len(numC) - 1] = numC[len(numC) - 1] - 1
	
	print currentTime, numC[len(numC) - 1], len(ucl)
	
	if numC[len(numC) - 1] <= 0:
		break

print numS, numI, numR, cumI, numC
