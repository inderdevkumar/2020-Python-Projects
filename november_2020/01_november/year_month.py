import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_excel("data.xlsx")

list_of_may_from_df= df['May'].to_list()
list_of_may= [0 if x== "T" else x for x in list_of_may_from_df]
df["new_may"]=  list_of_may

list_of_oct_from_df= df['Oct'].to_list()
list_of_oct= [0 if x== "T" else x for x in list_of_oct_from_df]
df["new_oct"]=  list_of_oct

df = df.drop(['May','Oct'], axis=1)
column_names = ['Season', 'Jan','Feb','Mar','Apr', 'new_may', 'Jun' , 'Jul', 'Aug' , 'Sep', 'new_oct', 'Nov', 'Dec']
df= df.reindex(column_names,axis=1)

df= df.set_index("Season")

df = df.rename(columns={'Jan':"January", 'Feb': "February", 'Mar':"March", 'Apr':"April",'new_may': "May",'Jun': "June",'Jul': "July",
           'Aug':"August", 'Sep':"September", 'new_oct':"October",'Nov':"November", 'Dec':"December"})


def plot_pie():    
    df.plot(kind = 'pie', y= user_input, figsize=(12, 12))
    plt.title(f"Inches of snow by Year for {user_input}")
    plt.show()

choice= 1
while choice:
    
    print("Here are the month with snowfall data: \n")
    for month in df.columns:        
        print(month)
        
    user_input= input("Enter a month you would like to view: ")
    if user_input in df.columns:
##        for month_value in df.columns:
##            sum_of_month= df[month_value].sum()
##            print(sum_of_month)
        if (user_input == "June" or user_input == "July" or user_input == "August" or user_input == "September"):
            choice= 1
            print("Case3")
            print(f"No Snowfall data was found for month of {user_input}")
            
        
        else:
            print("Case1")
            choice= 0
            plot_pie()
            
            
    else:
        print("Case2")
        print("Column not found , please try again \n")
        continue
        
