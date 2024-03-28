import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
fig, ax = plt.subplots()
start = 0
TLSV13 = 74.4
TLSV12 = 25.6
ax.broken_barh([(start, TLSV13), (TLSV13, TLSV13+TLSV12), (TLSV13+TLSV12, TLSV13+TLSV12)], [10, 9], facecolors=('#90EE90', '#ADD8E6', '#FDB200'))
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
ax.text(30, 14.5, "TLSv1.3: 74.4%", fontsize=15)
ax.text(75, 14.5, "TLSv1.2: 25.6%", fontsize=1)
leg1 = mpatches.Patch(color='lightgreen', label='TLSV1.3')
leg2 = mpatches.Patch(color='lightblue', label='TLSV1.2')
#ax.legend(handles=[leg1, leg2], ncol=3)
plt.savefig('Mhome_captures/graphs/TLSV13_vs_TLSV12.pdf')
plt.show()