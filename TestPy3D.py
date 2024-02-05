from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from random import randint

fig = plt.figure()

ax = plt.axes(projection ='3d')

triangle = [[500, 0, 430], [0, 860, 0], [1000, 860, 0], [500, 860, 860]]
start = [500, 20, 430]

for x in range(1000):
    ax.scatter(start[0], start[1], start[2], color='black', s=2)
    corner = randint(0,3)
    start = [(triangle[corner][0]+start[0])/2, (triangle[corner][1]+start[1])/2, (triangle[corner][2]+start[2])/2]

ax.set_title('Sierpinski Triangle')
plt.show()