import matplotlib as plt

plt.rc('text', usetex = False)
plt.rc('font', size = 14, family = 'serif', serif = ['STIXGeneral'])
plt.rc('xtick', labelsize = 'small')
plt.rc('ytick', labelsize = 'small')
plt.rc('legend', frameon = True, fontsize = 'medium', loc = "best")
plt.rc('figure', figsize = (10, 6), facecolor = "white")
plt.rc('lines', linewidth=1.0)
plt.rc('axes', xmargin = 0, ymargin = 0, autolimit_mode = 'round_numbers', grid=False)
plt.rc('mathtext', fontset = 'cm', rm = 'serif')