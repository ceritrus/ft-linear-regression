import matplotlib.pyplot as plt
import numpy as np
import csv

xaxis = []
yaxis = []

with open('data.csv', 'r') as datafile:
	for line in datafile:
		if line == 'km,price\n':
			continue
		mileage, price = line.split(',')
		yaxis.append(int(price))
		xaxis.append(int(mileage))

n = np.size(xaxis)
xmean = np.mean(xaxis)
ymean = np.mean(yaxis)
sx = np.std(xaxis)
sy = np.std(yaxis)
r = np.sum((xaxis - xmean) * (yaxis - ymean)) / (n * sx * sy)
m = r * sy / sx
c = ymean - m * xmean




plt.plot(yaxis, xaxis, 'bP')
plt.title('Linear Regression')
plt.xlabel('X - Mileage')
plt.ylabel('Y - Price')
plt.show()
