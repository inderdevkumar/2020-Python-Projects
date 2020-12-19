import pandas as pd  #pip install pandas
import matplotlib.pyplot as plt #pip install matplotlib
import numpy as np  #pip install numpy

#If you are still facing issue, please try to install other dependent package

df= pd.read_excel("MONTH_wise.xlsx")  #Data stored in excel format, same data as given in question with 2 columns amount and month

amount_positive_df = df.loc[df['amount'] > 0]
amount_negative_df = df.loc[df['amount'] < 0]

#For Positive Amount
Month_Wise_positive= amount_positive_df.groupby(by=["month"])  #Grouping data by month to Calculate mean month wise
month_wise_positive_mean= Month_Wise_positive['amount'].mean()  #Calculate mean
month_wise_positive_mean.to_excel("positive_amount.xlsx")  #Importnat to save in another excel as without changig might give error
positive_df= pd.read_excel("positive_amount.xlsx")  #Read newly saved grouped by data. This data will have 2 columns but with 3 rows as only 3 unique months are present in original data
print(positive_df)
new_month = ["January","February","March"]  #List to replace month name "1" with "January" , "2" with "February" ....... and so on
positive_df['new_month'] = new_month #Saving this column in new dataframe

#For Negative Amount
Month_Wise_negative= amount_negative_df.groupby(by=["month"])  #Grouping data by month to Calculate mean month wise
month_wise_negative_mean= Month_Wise_negative['amount'].mean()  #Calculate mean
month_wise_negative_mean.to_excel("negative_amount.xlsx")  #Importnat to save in another excel as without changig might give error
negative_df= pd.read_excel("negative_amount.xlsx")  #Read newly saved grouped by data. This data will have 2 columns but with 3 rows as only 3 unique months are present in original data
print(negative_df)
negative_df['new_month'] = new_month #Saving this column in new dataframe


#For bar graph

x = np.arange(3)
ax1 = plt.subplot(1,1,1)
w = 0.2
#plt.xticks(), will label the bars on x axis with the respective Month names.
plt.xticks(x + w /2, positive_df['new_month'], rotation='vertical')

positive_mean =ax1.bar(x, positive_df['amount'], color='b', width = w, align='center')
#The trick is to use two different axes that share the same x axis, we have used ax1.twinx() method.
ax2 = ax1.twinx()
#For Negative Mean
negative_mean =ax2.bar(x + w, negative_df['amount'], width=w,color='g',align='center')
#Set the Y axis label as Mean Amount.
plt.ylabel('Mean Amount')
#To set the legend on the plot we have used plt.legend()
plt.legend([positive_mean, negative_mean],['Positive Month- wise mean', 'Negative Month- wise mean'])
#To show the plot finally we have used plt.show().
plt.title("Month wise Mean") #Title of my plot
plt.show()
