import numpy
import matplotlib.pyplot as plt
<<<<<<< HEAD
ds1=numpy.random.uniform(1,9,10) #data distribution

#gaussian or normal data distribution ie) bell curve
ds=numpy.random.normal(1,5,40000)
print(ds)

x=[5,6,7,8]
y=[1,2,3,0]
#to display histogram
plt.hist(ds,100)
=======
#ds=numpy.random.uniform(1,9,10) #data distribution
#gaussian or normal data distribution ie) bell curve
ds=numpy.random.normal(1,5,40000)
print(ds)
x=[5,6,7,8]
y=[1,2,3,0]
#to dip histogram
#plt.hist(ds,100)
>>>>>>> 493a0b7 (other files)

#scatter plot
plt.scatter(x,y)
plt.show()

