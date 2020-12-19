import pandas as pd

df= pd.read_csv("template.txt" ,sep=",")
print(df)
global user_item_id, choice

user_item_id= 0
choice= 1


def main():
    pass


main()

def checkout():
     
    print("Thanks for shopping at Amazing")
    print("Your Purchaed the folowing items: ")
    try:
        print(f"{user_item_id}")     
        print(f"The Amount is: ${user_item_id[3]}")
    except:
        print("Please add the item to the cart")
def chosen_category():
    global user_input
    
    filter_choice= input("Enter 'yes' for applying Filter on customer rating: ")

    #print list of filtered items
    if (filter_choice== "yes"):
        selected_category_df= (df.loc[(df['category'])== user_input])  #Filtered category
        
        user_rating= float(input("Please enter the minimum rating: "))
        
        filtered_rating_df= (selected_category_df.loc[(selected_category_df['category']== user_input) &  (selected_category_df['avg custome rating'] >= user_rating)])
        item_id_list= list(filtered_rating_df.item_id)
        print(f"Item ID  Information: {item_id_list}")
        user_item_id= input("Please input Item ID or type any key to return: ")
        
        if (user_item_id in item_id_list):
            list_item_id= ((df.loc[(df['item_id'])== user_item_id])).values.tolist()
            print(f"Item ID {user_item_id} Information: {list_item_id}")
            print(f"{user_item_id} added to the cart")

        else:
            start()
            


def start():

    global user_input, choice

    print("Welcome to shopping at Amazing")
    category_list= list(df.category)
    print("we sell items in the following categories: ", category_list)
    while choice:
        user_input= input("Please enter a category name or input 'checkout' to quit: ").lower()
        
        #Get list of category
        
        
        if (user_input == "checkout"):
            choice= 0
            checkout()
            
        elif (user_input in category_list):
           choice= 0
           chosen_category()
           
        else:
            
            continue
 

if __name__ == "__main__":
    start()

   

