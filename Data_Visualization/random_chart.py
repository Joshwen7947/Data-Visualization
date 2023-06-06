from random import *
import matplotlib.pyplot as plt

class RandomChart:
    def __init__(self,num_points=5000):
        self.num_points = num_points
        self.x_val = [0]
        self.y_val = [0]
        
    def fill(self):
        while len(self.x_val) < self.num_points:
            x_way = choice([1,-1])
            x_dist = choice([1,2,3,4])
            x_step = x_way*x_dist
            
            y_way = choice([1,-1])
            y_dist = choice([1,2,3,4])
            y_step = y_way *y_dist
            
            if x_step == 0  and y_step == 0:
                continue
            
            x = self.x_val[-1] + x_step
            y = self.y_val[-1]+y_step
            self.x_val.append(x)
            self.y_val.append(y)
         
run = input("Make a chart (y/n): ")
while run != "n":              
    rc = RandomChart(100_000)
    rc.fill()

    plt.style.use('classic')
    fig,ax = plt.subplots()
    point_numbers = range(rc.num_points)
    ax.scatter(rc.x_val,rc.y_val,c=point_numbers,cmap=plt.cm.Reds,edgecolors="none", s=1)

    plt.savefig("random_chart.png")
    plt.show()     
    
    run = input("Make another (y/n): ")