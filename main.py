import numpy as np
import matplotlib.pyplot as plt


# attributes to sin(x) plot
domain_length = 5*(2*np.pi)  # 5 periods
max_frequency = 2*np.pi

nyquist_rate = 2 * (1/max_frequency) * domain_length
nyquist_rate = int(np.floor(nyquist_rate+1))


fig, axs = plt.subplots(4, 1, constrained_layout=True)  # constrained_layout to prevent overlap
fig.supxlabel("sample interpolation")
fig.supylabel("signal")


# oversampled (reference)

x = np.linspace(0, domain_length, 1000)
y = np.sin(x)

for ax in axs:
	ax.plot(x, y, linewidth=2)
	ax.set_xticks([])
	ax.set_yticks([])

axs[0].set_xlabel('oversampled (reference)')


# 2 * nyquist rate (safety margin)

x = np.linspace(0, domain_length, 2*nyquist_rate)
y = np.sin(x)

axs[1].plot(x, y, marker='.')

axs[1].set_xlabel('2 * nyquist rate (safety margin)')


# nyquist rate (technically minimum)

x = np.linspace(0, domain_length, nyquist_rate)
y = np.sin(x)

axs[2].plot(x, y, marker='.')

axs[2].set_xlabel('nyquist rate (technically minimum)')


# under nyquist rate (undersampled, aliased)

x = np.linspace(0, domain_length, int(0.9*nyquist_rate))
y = np.sin(x)

axs[3].plot(x, y, marker='.')

axs[3].set_xlabel('under nyquist rate (undersampled, aliased)')


# show

plt.show()
