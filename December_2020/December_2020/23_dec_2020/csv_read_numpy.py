import numpy as np



def summarize():

    records = np.loadtxt('data.csv', delimiter="\t", dtype='str,int', unpack=True)
    print(records[:])
summarize()

