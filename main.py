import numpy as np
import matplotlib.pyplot as plt
import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c; "))

# Using Numpy to create an array X
X_log = np.arange(0.000000001, 100)
y_for_log = []
for i in X_log:
    y_for_log.append(math.log(i))

X_q = np.arange(-100, 100)
y_for_q = []

for i in X_q:
    y_for_q.append(int((a*(i**2))+(b*i) +c))


fig, ax = plt.subplots()

ax.plot(X_log, y_for_log, color='r', label='lg')
ax.plot(X_q, y_for_q, color='g', label='ax^2 +bx +c')

ax.set_aspect('equal')
ax.grid(True, which='both')

# set the x-spine (see below for more info on `set_position`)
ax.spines['left'].set_position('zero')

# turn off the right spine/ticks
ax.spines['right'].set_color('none')
ax.yaxis.tick_left()

# set the y-spine
ax.spines['bottom'].set_position('zero')

# turn off the top spine/ticks
ax.spines['top'].set_color('none')
ax.xaxis.tick_bottom()

# Adding legend, which helps us recognize the curve according to it's color
plt.legend()

# To load the display window
plt.show()




