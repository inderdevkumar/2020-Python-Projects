import pandas as pd

df= pd.read_csv("cancer_data.csv")
print(df.head())

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) >=2:
        sex = line[1]
        age = line[2]

        print('%s\t%s' % (sex, age))