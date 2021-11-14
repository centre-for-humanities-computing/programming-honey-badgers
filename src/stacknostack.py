import numpy as np
import matplotlib.pyplot as plt

filename = 'dat/series/series-01.csv'
data = np.loadtxt(fname=filename, delimiter=',')
data = data[:10, :]

# stacked
fig = plt.figure(figsize=(20, 4))
for series in data:
    plt.plot(series, c='black')
plt.xlabel('Time')
plt.ylabel('Intensity')
plt.title('Stacked Series')
plt.savefig('figs/stacked.png')

# unstacked
m, n = data.shape 
fig, axes = plt.subplots(m, 1, figsize=(20, 4*m), sharex=True)
for (i, series) in enumerate(data):
    axes[i].plot(data.T, c='gray', alpha=.5)
    axes[i].plot(series, linewidth=3, c='black')
    axes[i].set_ylabel('Intensity', fontsize=25)

axes[i].set_xlabel('Time', fontsize=25)
axes[0].set_title('Unstacked Series', fontsize=30)
plt.tight_layout()
plt.savefig('figs/unstacked.png')
