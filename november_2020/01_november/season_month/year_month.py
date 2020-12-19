import pandas as pd
import matplotlib.pyplot as plt

#To draw pie chart
def plot_pie():
    
    global df, user_input
    df.plot(kind = 'pie', y= user_input, figsize=(12, 12))
    plt.title(f"Inches of snow by Year for {user_input}")
    plt.show()


def user_choice():
    
    global df, user_input
    #Import my data 
    df = pd.read_excel("data.xlsx")

    #---------------------------------------------------------------------------------------------
    #Replacing 'T' of May with 0
    list_of_may_from_df= df['May'].to_list()
    list_of_may= [0 if x== "T" else x for x in list_of_may_from_df]
    df["new_may"]=  list_of_may

    #Replacing 'T' of May with 0
    list_of_oct_from_df= df['Oct'].to_list()
    list_of_oct= [0 if x== "T" else x for x in list_of_oct_from_df]
    df["new_oct"]=  list_of_oct

    #Adding a column of new_season with the help of list as per pie chart shown in diagram
    df["new_season"]= ["2000-01","2001-02","2002-03","2003-04","2004-05","2005-06","2006-07","2007-08","2008-09","2009-10"]


    #Drop columns of May/Oct/Season
    df = df.drop(['May','Oct', 'Season'], axis=1)

    #Reordeing columns as 
    column_names = ['new_season', 'Jan','Feb','Mar','Apr', 'new_may', 'Jun' , 'Jul', 'Aug' , 'Sep', 'new_oct', 'Nov', 'Dec']
    df= df.reindex(column_names,axis=1)

    #Set index 
    df= df.set_index("new_season")

    df = df.rename(columns={'Jan':"January", 'Feb': "February", 'Mar':"March", 'Apr':"April",'new_may': "May",'Jun': "June",'Jul': "July",
               'Aug':"August", 'Sep':"September", 'new_oct':"October",'Nov':"November", 'Dec':"December"})
    #---------------------------------------------------------------------------------------------------------------------------
    choice= 1    
    while choice:
        
        print("Here are the month with snowfall data: \n")
        for month in df.columns:        
            print(month)

        #CASE3  
        user_input= input("Enter a month you would like to view: ")
        if user_input in df.columns:
            if (user_input == "June" or user_input == "July" or user_input == "August" or user_input == "September"):
                choice= 1
                print("Case3")
                print(f"No Snowfall data was found for month of {user_input}")
                
          #CASE1  
            else:
                print("Case1")
                choice= 0
                plot_pie()
                
          #CASE2      
        else:
            print("Case2")
            print("Column not found , please try again \n")
            continue

if __name__ == "__main__":
    user_choice()       
