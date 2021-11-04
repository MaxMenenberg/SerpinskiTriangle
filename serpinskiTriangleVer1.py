import matplotlib.pyplot as plt
import numpy as np
import time
plt.ion()

# Source for this class example
# https://stackoverflow.com/questions/10944621/dynamically-updating-plot-in-matplotlib
class DynamicUpdate():
    #Suppose we know the x range
    min_x = 0
    max_x = 10
    

    def on_launch(self, L):
        #Set up plot
        scaleFactor = 0.2
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([],[], 'yo', markersize = 1)
        self.ax.set_facecolor((27/255, 82/255, 29/255))
        #Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
        self.ax.set_xlim(0-L*scaleFactor, L*(1+scaleFactor))
        self.ax.set_ylim(0-L*scaleFactor, np.sqrt(3)*L*(1+scaleFactor)/2)

    def on_running(self, xdata, ydata, n, N):
        #Update data (with the new _and_ the old points)
        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)
        #Need both of these in order to rescale
        self.ax.relim()
        self.ax.autoscale_view()
        self.ax.set_title('Drawing point {0} of {1}'.format(n,N), 
             fontsize = 14)
        #We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    #Example
    def __call__(self, L, N, t):
        
        plt.close('all')
        self.on_launch(L)
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
        self.on_running(xdata, ydata, 0, N)
        
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
            self.on_running(xdata, ydata, n+1, N)
            
            currentX = newX
            currentY = newY
            
           # If you want to plot slower you can uncomment out this line
           # however time.sleep cant really pause for times shoter than 10ms
            time.sleep(1)
        
        return xdata, ydata

L = 1000;    # Size of the serpinski triangle to draw
N = 2000;   # Number of points to draw
t = 0.00001;
d = DynamicUpdate()
d(L, N, t)