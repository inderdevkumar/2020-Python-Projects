import pandas as pd  #pip install pandas

df= pd.read_csv("Covid Data.txt")  #Reading my text file

choice= 1
while choice:
    
    user_input= input("\nPlease enter the name of a city/county: ")  #Ask the user for the name of a city/county 
    
    Locality_list= df["Locality"].tolist()  #Converting "Locality" column of dataframe into list to check if user_input exist in the Locality_list 

    if (user_input in Locality_list):
        #print("Columns are: ",df.columns)

        #======================= Part 1:  ===========================
        county_df = df[df['Locality'] == user_input]  # Getting dataframe where user_input == Locality
        #print(county_df)  #Your output will be many lines long. I have commented it
        print(county_df.head())  #This is just for demo which will show only top5 dataframe
        print("\nShape of my dataframe is: ", county_df.shape)  #This will show long data is. Rows and columns are printed
        
        #=======================  Part 2 ==================================
        date_and_max_cases= county_df[['Report Date', 'Total Cases']][county_df["Total Cases"] == county_df["Total Cases"].max()]  #Getting maxcases and date for the user input city
        print(f"\ndate and max cases for the city/county {user_input} is: \n", date_and_max_cases)


        #=======================  Part 3 ==================================
        health_districts= df["VDH Health District"].tolist()   #Converting "VDH Health District" column of dataframe into list
        choice= 0
        unique = [] 
        for item in health_districts:
            #Logic for uniqueness
            if item not in unique: 
                unique.append(item)

        
        
        
        print("\nHealth District are:\n",  unique)
    else:
        continue
