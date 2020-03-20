import numpy as np
from matplotlib import pyplot as plt
import datetime
from scipy import interpolate

# csvファイルからデータを読み込み
data = np.loadtxt('/Users/moritatarou/Desktop/2020NCTS10Z-Nb3SnLayerThickness.csv', skiprows=1, delimiter=',')

temp = data[:, 0]  # temperature data
aveth = data[:, 1]  # Nb3Sn layer thickness data
std = data[:, 2]  # standard deviation data

#fig = plt.figure(figsize=(8,5), tight_layout=True)
#ax = fig.add_subplot(1,1,1)

# グラフの初期化
fig, ax = plt.subplots(figsize=(8,8), tight_layout=True)

#  データをプロット（エラーバー付きグラフ）
ax.errorbar(temp, aveth, yerr=std, capsize = 8, fmt = 'o', \
        label= r'2020N-CT-S10Z (400$^\circ$C $\times$ 100 h pre-annealing)')

fig.show()

# label setting
ax.set_xlabel(r'Temperature ($^\circ$C)', fontsize=18)
ax.set_ylabel(r'Nb$_3$Sn layer thickness ($\mu$m)', fontsize=18)

# 軸の範囲の設定
ax.set_xlim(670, 730)  # x軸の範囲を設定
ax.set_ylim(0,45)  # y軸の範囲を設定 

# axis setting
ax.xaxis.set_ticks_position('both') # x軸を両側に配置
ax.yaxis.set_ticks_position('both') # ｙ軸を両側に配置

ax.minorticks_on() # 副軸を表示
ax.tick_params(axis='both', which='both', direction='in', labelsize = 14,\
        pad=10, width=2)

ax.tick_params(axis='both', which='minor', length=5) # 主軸の長さを設定
ax.tick_params(axis='both', which='major', length=8) # 副軸の長さを設定

# グラフ枠の太さの設定
# for文でtop, bottom, left, rightに対してそれぞれ太さを一括で設定
for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2)
ax.legend(loc='lower right', fontsize =14, borderaxespad=1)

#plt.show()
plt.savefig('figure.pdf', dpi=300) # 図をdpi=300でpdfファイルで保存
