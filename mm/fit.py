import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#init
#x1=np.linspace(4000,4016,17)
#x2=np.linspace(4076,4100,25)
#y=np.empty(56)
odr=4 #number of order

#read data
dt=pd.read_table('ws4.23.txt',sep='\s+',header=None) #input data
x=dt[0]
y=dt[1]
#x3=dt[0]
#y[17:31]=dt[1]
#x=np.append(x1,x3)
#x=np.append(x,x2)
plt.scatter(x,y,label='origin dt')

#fit
a=np.polyfit(x,y,odr)
b=np.poly1d(a)
c=b.coeffs
for i in range(0,odr+1):
    print(c[i])
print(b)
print(c)

xx=np.linspace(4016,4076,601)
yy=np.empty(601)
fo=open('out.txt','w')
for i in range(0,601):
    yy[i]=b(xx[i])
    fo.write(str(xx[i])+'\t'+str(yy[i])+'\n')
    
plt.scatter(xx,yy,s=2,c='r',label='scat after fit')
#plt.plot(x,b(x),ls='--',c='red',label='fit by dt1')
plt.legend()
plt.savefig('png.png')
plt.show()
