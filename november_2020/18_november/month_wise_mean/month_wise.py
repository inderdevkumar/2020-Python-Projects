import pandas as pd  #pip install pandas
import matplotlib.pyplot as plt #pip install matplotlib

#If you are still facing issue, please try to install other dependent package

df= pd.read_excel("MONTH_wise.xlsx")  #Data stored in excel format, same data as given in question with 2 columns amount and month
Month_Wise= df.groupby(by=["month"])  #Grouping data by month to Calculate mean month wise
month_wise_mean= Month_Wise['amount'].mean()  #Calculate mean
month_wise_mean.to_excel("test.xlsx")  #Importnat to save in another excel as without changig might give error

new_df= pd.read_excel("test.xlsx")  #Read newly saved grouped by data. This data will have 2 columns but with 3 rows as only 3 unique months are present in original data
print(month_wise_mean)

new_month = ["January","February","March"]  #List to replace month name "1" with "January" , "2" with "February" ....... and so on
new_df['new_month'] = new_month #Saving this olumn in new datframe

amount= new_df['amount'].values.tolist()  #Converting  column "amount" into list
month= new_df['new_month'].values.tolist()  #Converting  column "new_month" into list



fig = plt.figure(figsize = (8, 4)) #Zize of plot
# creating the bar plot 
plt.bar(month, amount, color ='maroon',width = 0.2)  #Width of bar graph with month in x-axis and amount(mean amount) column in Y-axis

plt.xlabel("Month Name") #Label in x-axis
plt.ylabel("Mean") #Label in y-axis
plt.title("Month wise Mean") #Title of my plot
plt.show() #Showing plot
