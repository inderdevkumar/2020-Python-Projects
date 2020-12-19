import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_excel("data.xlsx")
df["May"].fillna(0, inplace = True)
df["Oct"].fillna(0, inplace = True)

april_month= (df['Apr'].astype(str).values.tolist())    
april_res = [sub.replace(' T', '') for sub in april_month]
april_float_res = [float(ele) for ele in april_res]
df["new_april"]=  april_float_res

sept_month= df['Sep'].astype(str).values.tolist()
sept_res= [sub.replace(' T', '') for sub in sept_month]

sept_float_res = [float(ele) for ele in sept_res]
df["new_sep"]=  sept_float_res

df = df.drop(['Apr','Sep'], axis=1)

df= df.set_index("Season")

df = df.rename(columns={'Jan':"January", 'Feb': "February", 'Mar':"March", 'new_april':"April",'May': "May",'Jun': "June",'Jul': "July",
           'Aug':"August", 'new_sep':"September", 'Oct':"October",'Nov':"November", 'Dec':"December"})

def plot_pie():    
    df.plot(kind = 'pie', y= user_input, figsize=(12, 12))
    plt.title(f"PIE Chart for {user_input}")
    plt.show()

choice= 1
while choice:
    user_input= input("Enter a month you would like to view: ")
    if user_input in df.columns:
        choice= 0
        plot_pie()
        
    else:
        
        continue
        
