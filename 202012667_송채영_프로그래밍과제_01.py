import matplotlib.pyplot as plt
import numpy as np

def line(ax, pos, *args, **kwargs):
    if ax == 1:
        for p in pos:
            plt.axvline(p, *args, **kwargs)
    else:
        for p in pos:
            plt.axhline(p, *args, **kwargs)

input = [0,1,0,0,1,1,0,0,0,1,1]
        
data = np.repeat(input, 2)
clock = 1 - np.arange(len(data)) % 2
manchester = np.logical_xor(clock, data)
differential_manchester = np.repeat(input, 2)
for i in range(1, 22):
        if i % 2 == 0:
            if differential_manchester[i] == 0:
                differential_manchester[i] = 0 
                if differential_manchester[i-1] == 0:
                    differential_manchester[i] = 1
            else:
                differential_manchester[i] = differential_manchester[i-1]
        else:
            differential_manchester[i] = 0 
            if differential_manchester[i-1] == 0:
                differential_manchester[i] = 1

tap = 0.5 * np.arange(len(data))

line(1, range(11), color='.7', linewidth=2)
line(2, [0.5,4], color='.7', linewidth=2)
plt.step(tap, manchester+3.5, 'black', linewidth = 2, where='post')
plt.step(tap, differential_manchester, 'black', linewidth = 2, where='post')
plt.ylim([-1,6])

for tb, b in enumerate(input):
    plt.text(tb + 0.4, 6, str(b))
str='manchester'
str2='differential_manchester'
plt.text(0, 5, str)
plt.text(0, 2, str2)

plt.gca().axis('off')
plt.show()
