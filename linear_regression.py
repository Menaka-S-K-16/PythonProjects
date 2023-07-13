import numpy
import matplotlib.pyplot as plt
from scipy import stats

x = numpy.random.uniform(1,9,30)
y = numpy.random.uniform(2,19,30)

#print(stats.linregress(x,y)) it gives 6 values

slope, intercept, r,p, stderr =stats.linregress(x,y)

#line function mx + intercept
def myfunc(x):
    return slope*x + intercept
#to pass each x value it myfunc
mymodel = list(map(myfunc , x))

plt.scatter(x, y) #original
plt.plot(x, mymodel) #after applying line function
plt.show()