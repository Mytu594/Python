# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import matplotlib.cm
import random 
import squarify


x = 0.
y = 0.
width = 1050.
height = 733.


fig = plt.figure(figsize = (12,10))
ax = fig.add_subplot(111,fc='white')

initvalues = [285.4,188.4,173,140.6,91.4,75.5,62.3,39.6,29.4,28.5,26.2,22.2]
values = initvalues
values.sort(reverse = True)
values = squarify.normalize_sizes(values,width,height)

labels = ["South Africa","Egypt","Nigeria","Algeria","Morocco","Angola","Libya","Tunisia","Kenya","Ethiopia","Ghana","Cameron"]

colors = [(214,27,31),(229,109,0),(109,178,2),(50,155,18),(41,127,214),(27,70,163),(72,17,121),(209,0,89),(148,0,26),(223,44,13),(195,215,0)]
for i in range(len(colors)):
    r,g,b = colors[i]
    colors[i] = (r/255. , g/255. , b/255.)

cmap = matplotlib.cm.get_cmap()
color = [cmap(random.random()) for i in range(len(list(values)))]


idx = 1
label=[]
for l in labels:
    s=str(idx)+"-->"+l
    label.append(s)
    idx=idx+1

value=["($"+str(v)+"b)" for v in initvalues]

plot = squarify.plot(sizes=values,color=colors,label=label,value=value,norm_x = 1100,norm_y = 800)
plot.set_title('非洲GDP排前12名的国家',fontdict={'fontsize':18})
plt.rc('font',size=12)#标签大小
plt.show()