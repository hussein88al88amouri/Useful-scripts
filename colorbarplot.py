import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
fig, ax = plt.subplots(1, 1,figsize=(1,8))
fraction=1
norm = mpl.colors.Normalize(vmin=0, vmax=1)
cbar = ax.figure.colorbar(
            mpl.cm.ScalarMappable(norm=norm, cmap=sns.color_palette("light:b_r", as_cmap=True)),
            ax=ax,fraction=fraction)
plt.tight_layout()
ax.axis('off')
plt.show()
path=""
plt.savefig(path,bbox_inches='tight',pad_inches=0)
