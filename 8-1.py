import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
AutoMinorLocator)
import numpy as np

#здесь пишется реализация чтения данных. Можно взять следующее:
#    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#with open ('settings.txt') as settings:
#    tmp = [float(i) for i in settings.read().split("\n")]
#data_array = 3.3/2**8*np.loadtxt('Boris.txt', dtype = int)
#t= (0.9408938180316578)*np.arange(len(data_array))
#X = t
#Y = data_array
#    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#тогда вместо значений по х и по y подставляете просто X,Y
#так же свои данные вписывайте в значение по t.

fig, ax = plt.subplots(figsize=(16,10), dpi=400)
#xax= ax.xaxis # не особо уверен в этих двух строчках
#yax= ax.yaxis # разкоменчивать вместе с строками 37-38
#plt.xlim(0, 42)
#plt.ylim(0, 3)
ax.set_title('YOURNAMEOFGRAPH', fontsize=18)
ax.set_xlabel('NAMEYOUR"X"', fontsize=12)
ax.set_ylabel('NAMEYOUR"Y"', fontsize=12)
plt.grid(True)
ax.grid(which='major', linewidth=1.2, color='black')
ax.grid(which='minor', linestyle='--', color='gray', linewidth=0.5)
#plt.xticks(np.arange(min(x), max(x)+1, 5.0)) #здесь ставятся точки с интерваломпоследнее число в скобках - шаг между точками
#ax.scatter([16.79, 20.51, 25.45, 31.95, 39.59],[8.59, 10.47, 13.06, 16.35, 20.20]) #в этой строке ставятся точки, если вам нужно ставить не все точки, разкомментьте предыдущую строчку и подставьте свои данные
ax.plot([16.79, 20.51, 25.45, 31.95, 39.59], [8.59, 10.47, 13.06, 16.35, 20.20], label=u'NAMEFORLEGEND', color='olivedrab', marker='>', markersize = '5') #здесь ваши данные
ax.plot(0,0,label=u'time=41.399327993392944c', color='white', marker ='.', markersize='0') #если нужно поставить особую точку на графике и выделить её цветом/формой. Сейчас выделяться ничего не будет    
plt.text(0.93, 0.9, 'NAMEFORYOURTEXT', fontsize=14, horizontalalignment='right', verticalalignment='center', color='maroon', transform=ax.transAxes) #если где-то на графике требуется пояснение
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='major', length=10, width=2)
ax.tick_params(which='minor', length=5, width=1)
plt.legend()
#xax.set_minor_locator(ticker.MultipleLocator(1))
#yax.set_minor_locator(ticker.MultipleLocator(1))

fig.savefig('NAMEFORYOURFAILE.png')
plt.show()
