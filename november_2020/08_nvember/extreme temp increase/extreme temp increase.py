import pandas as pd

df= pd.read_excel("AirQualityUCI.xlsx")

df.drop(df.columns[[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14]], axis = 1, inplace = True)

new_df= df.loc[(df['T']>= -5) & (df['T']<= 50)]
               
print(new_df.head(15))
