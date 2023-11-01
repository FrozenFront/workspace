import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
with open ('settings.txt') as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
data_array = 3.3/2**8*np.loadtxt('Boris.txt', dtype = int)
t= 0.9408938180316578*np.arange(len(data_array))
x = t
y = data_array
fig, ax = plt.subplots(figsize = (16, 10), dpi = 400)
xax= ax.xaxis
yax= ax.yaxis
plt.xlim(0, 42)
plt.ylim(0, 3)
ax.grid(which='major', color='black')
xax.set_minor_locator(ticker.MultipleLocator(1))
yax.set_minor_locator(ticker.MultipleLocator(1))
ax.minorticks_on()
ax.grid( which='minor')
plt.xlabel(u'Время С')
plt.ylabel(u'Напряжение В')
plt.title(u'RC цепочка')
plt.xticks(np.arange(min(x), max(x)+1, 5.0))
xax.get_ticklines(minor=True)
yax.get_ticklines(minor=True)
plt.text(0.93, 0.9, 'it`s just work!', fontsize=14, horizontalalignment='right', verticalalignment='center', color='maroon', transform=ax.transAxes)
ax.plot(x,y, label=u'Напряжение на RC цепочке', color='olivedrab', marker='>', markersize = '5')
ax.plot(0,0,label=u'time=41.399327993392944c', color='white', marker ='.', markersize='0')
plt.legend()
fig.savefig('BorisBorisovich.png')
plt.show()    
