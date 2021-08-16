import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

odr=4 #number of order
dt=pd.read_table('dt.txt',sep='\s+',header=None) #input data
x=dt[0]
y=dt[1]
plt.scatter(x,y,label='origin dt')

a=np.polyfit(x,y,odr)
b=np.poly1d(a)
c=b.coeffs
for i in range(0,5):
    print(c[i])
print(b)

xx=np.linspace(4000,4110,221)
yy=np.linspace(1,100,221)
fo=open('out.txt','w')
for i in range(0,221):
    yy[i]=b(xx[i])
    fo.write(str(xx[i])+'\t'+str(yy[i])+'\n')
    
plt.scatter(xx,yy,s=2,c='r',label='scat after fit')
#plt.plot(x,b(x),ls='--',c='red',label='fit by dt1')
plt.legend()
plt.savefig('png.png')
#plt.show()

