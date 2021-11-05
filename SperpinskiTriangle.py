import numpy as np
import matplotlib.pyplot as plt
import time 


N = 1000
L = 1

A = [0,0]
B = [L, 0]
C = [L/2, np.sqrt(3)*L/2]


currentX = np.random.rand(1)*L
currentY = np.random.rand(1)*np.sqrt(3)*L/2

xData = []
yData = []

xData.append(currentX)
yData.append(currentY)

for n in range(N):
    
    randomVertex = np.random.randint(0, 3);
    
    if randomVertex == 0:
        newX = (currentX + A[0])/2
        newY = (currentY + A[1])/2
    elif randomVertex == 1:
        newX = (currentX + B[0])/2
        newY = (currentY + B[1])/2
    else: 
        newX = (currentX + C[0])/2
        newY = (currentY + C[1])/2
        
    xData.append(newX)
    yData.append(newY)
    
    currentX = newX
    currentY = newY
    
    plt.plot(xData, yData, 'o', markersize = 0.5)
    plt.show()    
    time.sleep(1)
    

