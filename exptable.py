#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
---------------------------------------
@brief	expTable介绍
@author	jungle
@date	2016/01/05
---------------------------------------
'''

import math
import matplotlib.pyplot as plt

EXP_TABLE_SIZE = 1000
MAX_EXP = 6

expTable = [0 for i in range(0, EXP_TABLE_SIZE)]

print len(expTable)

for i in range(0, EXP_TABLE_SIZE):
    expTable[i] = math.exp(i * 1.0 / EXP_TABLE_SIZE * 2 - 1) * MAX_EXP
    expTable[i] = expTable[i] / (expTable[i] + 1)

print expTable

fig = plt.figure()

ax = plt.subplot(1,1,1)

## 设置坐标范围
plt.ylim(ymax=1.2)
plt.ylim(ymin=0.5)


## 绘制4条曲线.
ax.plot(expTable, label="exp")

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1])

plt.show()

