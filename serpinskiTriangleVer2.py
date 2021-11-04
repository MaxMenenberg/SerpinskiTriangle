import matplotlib.pyplot as plt
import numpy as np
import time

# Update a matplotlib plot in dynamically
# Source: # https://stackoverflow.com/questions/10944621/dynamically-updating-plot-in-matplotlib
def UpdatePlot(axis, points, fig, x, y, n, N):
    points.set_xdata(x)
    points.set_ydata(y)
    #Need both of these in order to rescale
    axis.relim()
    axis.autoscale_view()
    axis.set_title('Drawing point {0} of {1}'.format(n,N), 
         fontsize = 14)
    #We need to draw *and* flush
    fig.canvas.draw()
    fig.canvas.flush_events()

plt.ion()
plt.close('all')

ax = plt.subplots();
L = 1000;    # Size of the serpinski triangle to draw
N = 2000;    # Number of points to draw

scaleFactor = 0.2
figure, ax = plt.subplots()
points, = ax.plot([],[], 'yo', markersize = 1)
ax.set_facecolor((27/255, 82/255, 29/255))
ax.set_autoscaley_on(True)
ax.set_xlim(0-L*scaleFactor, L*(1+scaleFactor))
ax.set_ylim(0-L*scaleFactor, np.sqrt(3)*L*(1+scaleFactor)/2)

# Lists containing the x and y coordinates of the points in the triangle
xdata = []
ydata = []

# First define the 3 vertices of the triangle
A = np.array([0, 0])
B = np.array([L, 0])
C = np.array([L/2, np.sqrt(3)*L/2])

# Next randomly pic a starting point
startX = np.random.rand(1)*L;
startY = np.random.rand(1)*L*np.sqrt(3)/2

xdata.append(startX)
ydata.append(startY)

UpdatePlot(ax, points, figure, xdata, ydata, 0, N)

currentX = startX
currentY = startY

for n in range(N):
            
    # Randomly pick on of the 3 vertices of the 
    # try angle and compute the mid point from the
    # current point and the vertices
    
    randomVertex = np.random.randint(0,2+1);
    
    if randomVertex == 0:
        newX = (currentX + A[0])/2;
        newY = (currentY + A[1])/2;
    elif randomVertex == 1:
        newX = (currentX + B[0])/2;
        newY = (currentY + B[1])/2;
    else:
        newX = (currentX + C[0])/2;
        newY = (currentY + C[1])/2;     
        
    # Add the new point to the plot
    xdata.append(newX)
    ydata.append(newY)
    
    UpdatePlot(ax, points, figure, xdata, ydata, n, N)
            
    currentX = newX
    currentY = newY
     
    # If you want to plot slower you can uncomment out this line
    # however time.sleep cant really pause for times shoter than 10ms
    #time.sleep(t)

