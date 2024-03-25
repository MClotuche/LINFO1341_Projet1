import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
fig, ax = plt.subplots()
start = 0
IPv4 = 72.6
IPv6 = 27.4
ax.broken_barh([(start, IPv4), (IPv4, IPv4+IPv6), (IPv4+IPv6, IPv4+IPv6)], [10, 9], facecolors=('#90EE90', '#ADD8E6', '#FDB200'))
ax.set_ylim(5, 15)
ax.set_xlim(0, 100)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_yticks([15, 25])
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_axisbelow(True) 
ax.set_yticklabels([' ', ' '])
ax.grid(axis='x')
ax.text(30, 14.5, "IPv6: 72.6%", fontsize=14)
ax.text(75, 14.5, "IPv4: 27.64%", fontsize=13)
leg1 = mpatches.Patch(color='lightgreen', label='IPv4')
leg2 = mpatches.Patch(color='lightblue', label='TLSV1.2')
#ax.legend(handles=[leg1, leg2], ncol=3)
plt.savefig('Mhome_captures/graphs/IPv4_vs_IPv6.pdf')
plt.show()