import numpy as np
import pandas as pd

#vanguard = pd.read_table('https://www.dropbox.com/s/qqtpgrzslqhtcof/vanguard_stock_bond.csv?raw=1')

vanguard= pd.read_excel("vanguard.xlsx")
print(vanguard.head())

#============== Compute array sixty_forty that contains the returns to a monthly-rebalanced 60/40 portfolio =================================================

#Create Table vanguard2 that adds to the data in Table vanguard with a new column. That new column should have label sixty_forty and data the array you just created.

vanguard2= vanguard.set_index("Date")
vanguard2["sixty_forty"] = vanguard2.sum(axis=1)

print(vanguard2.head())

#Q2: Calculate the mean and SD of returns for VFINX.

VFINX_mean= vanguard2['VFINX'].mean()
VFINX_sd= vanguard2['VFINX'].std() 


#Q3: Calculate the mean and SD of returns for VBMFX.
VBMFX_mean= vanguard2['VBMFX'].mean()
VBMFX_sd = vanguard2['VBMFX'].std()

#Q4: Calculate the mean and SD of returns for sixty_forty.
sixty_forty_mean= vanguard2['sixty_forty'].mean()
sixty_forty_sd = vanguard2['sixty_forty'].std()
print(sixty_forty_mean, sixty_forty_sd)
