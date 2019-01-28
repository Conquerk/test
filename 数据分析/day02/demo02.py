import numpy as np
import matplotlib.pyplot as mp

mp.figure('Figure1',figsize=(4,3),facecolor='lightgray')
mp.figure('Figure2',figsize=(4,3),facecolor='black')
mp.figure('Figure1')
mp.title('Figure1',fontsize=18)
mp.xlabel('Date',fontsize=12)
mp.ylabel('Price',fontsize=12)
mp.tick_params(labelsize=8)
mp.grid(linestyle=':')
mp.tight_layout()
mp.show()