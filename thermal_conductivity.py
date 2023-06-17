import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
import numpy as np


h = 0.1
sigma = 1/6
k = sigma*h*h
length = 1
u_0_t = 0
u_l_t = 0
t_max = 1000
x_length = 100


def u_0(x):
    return 4*x*(1-x)


t_lst = np.linspace(0, t_max, t_max+1)*k
x_lst = np.linspace(0, length, x_length+1)
len_xi = np.arange(x_length+1)
u_lst = []
ui = [u_0_t]

for i in range(x_lst.size-2):
    ui.append(u_0(x_lst[i+1]))
ui.append(u_l_t)
u_lst.append(ui)

for j in range(t_lst.size):
    ui = []
    for i in range(x_lst.size):
        if i == 0:
            u_i_j = u_0_t
        elif i == x_lst.size-1:
            u_i_j = u_l_t
        else:
            u_i_j = sigma*(u_lst[j][i-1] + 4 * u_lst[j][i] + u_lst[j][i+1])
        ui.append(u_i_j)
    u_lst.append(ui)

fig, ax = plt.subplots(figsize=(14, 5), dpi=80)
phase = np.arange(t_max+1)
#plt.xlabel('Длина стержня', {'size': 16})
#plt.ylabel('Температура стержня', {'size': 16})
frames = []

plt.axis('off')
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)


for p in phase:
    y_plot = u_lst[p]

    #line, = ax.plot(x_lst, y_plot, c='k')
    line = ax.pcolormesh([y_plot], cmap='rainbow', vmin=0.100, vmax=1.000)
    frames.append([line])

animation = ArtistAnimation(
    fig,                # фигура, где отображается анимация
    frames,              # кадры
    interval=10,        # задержка между кадрами в мс
    blit=True,          # использовать ли двойную буферизацию
    repeat=True)       # зацикливать ли анимацию

animation.save('tempr_cmap.mp4')
animation.save('tempr_cmap.gif')

plt.show()

