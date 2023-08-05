import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.size']=16

Tc=2/np.log(1+np.sqrt(2))

n,T,steps=eval(input("L,T,steps? "))
nsq=n*n

plt.figure(figsize=(12,5))
s=np.random.randint(0,2,(n,n)) # 0 or 1
plt.subplot(1,2,1)
plt.imshow(s,origin='lower')
plt.xlabel('Starting configuration')
plt.suptitle('T={:.4g}'.format(T))
plt.xticks([]); plt.yticks([])

for i in range(1,steps*nsq+1):
    t=i/nsq
    x,y=np.random.randint(0,n,2)
    s_neighbors=s[(x+1)%n,y]+s[(x-1)%n,y]+s[x,(y+1)%n]+s[x,(y-1)%n]
    delE=8*(s_neighbors-2)*(s[x,y]-0.5)
    if delE<0 or np.random.rand()<np.exp(-delE/T):
        s[x,y]=int(not s[x,y])

plt.subplot(1,2,2)
plt.imshow(s,origin='lower')
plt.xticks([]); plt.yticks([])
plt.xlabel('Configuration after {} steps'.format(steps))
plt.tight_layout()

plt.show()
