#Import lybraries
import numpy as np
import matplotlib.pyplot as plt

#Define the function
def function(u):
    w=2.0*np.pi
    f=np.sin(w*u)
    return f

#Create a list which will be the rang of x
print('Introduce the bottom and the top limit of the integral in these order')
bottomlimit=float(input())
toplimit=float(input())
xlist=np.arange(bottomlimit,toplimit,0.01)

#Calculate the image of the variable
y=function(xlist)

#Create an empty list for dx and dy
xdev=[]
dy=[]

#Calculate the derivative and add the result to the list
i=0
imax=len(xlist)-1
while i<imax:
  diffx=xlist[i+1]-xlist[i]
  diffy=y[i+1]-y[i]
  dy.append(diffy/diffx)
  xdev.append(xlist[i])
  i=i+1

#Calculate the intergal
#I define the 'integrable as f(x)*dx where dx is the diferential
integrable=y*diffx
integral=sum(integrable)
print(integral)
#To have the expresion we hace to make a list
Fx=[]
xinter=[]
j=0
jmax=len(integrable)
inter=0
while j<jmax:
    inter=inter+integrable[j]
    Fx.append(inter)
    xinter.append(xlist[j])
    j=j+1

#Plot the result
plt.plot(xinter, Fx,'g', xlist, y)

#Add labels
plt.xlabel('x')
plt.ylabel('f(x),df(x)/dx and F(x)')
plt.title('Numerical calculation of derivative')
plt.legend(['f(x)','df(x)/dx','F(x)'])

#Show the plot
plt.show()






    
