import pandas as pd
df= pd.read_csv("Superstore.csv")

sum_of_sales= df['Sales'].sum()
sum_of_profit= df['Profit'].sum()

print("Total Sales: ", sum_of_sales)
print("Total Profits: ", sum_of_profit)

#uniue_Category= df['Category'].unique()

#Category wise Sales and profit
category_Wise= df.groupby(by=["Category"])
sum_of_sales_category= category_Wise['Sales'].sum()
sum_of_profit_category= category_Wise['Profit'].sum()

print("Total Sales for each category: ", sum_of_sales_category)
print("Total Profits for each category: ", sum_of_profit_category)

#Sales and profit for each state
State_Wise= df.groupby(by=["State"])
sum_of_sales_State= State_Wise['Sales'].sum()
sum_of_profit_State= State_Wise['Profit'].sum()

print("Total Sales for each state: ", sum_of_sales_State)
print("Total Profits for each state: ", sum_of_profit_State)


#The best-selling Sub-category for each state

sub_cagtegory_Wise_state= df.groupby(["State", 'Sub-Category'])
sum_of_sales_sub_cagtegory= sub_cagtegory_Wise_state['Sales'].max()

print("The best-selling Sub-category for each state: ", sum_of_sales_sub_cagtegory)




