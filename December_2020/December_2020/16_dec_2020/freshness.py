#==================== For List Function Defination  ========================================
def fresh(list_of_num ):

   
    #============  Logic for 1D or 2D  List  ===================================

    #=========== If 2D ======================================
    if isinstance(list_of_num[0], list):
        print("\nFor 2D List: ", list_of_num)

        #==============   Logic Used to find freshness  =====================================
        for value in list_of_num:
            count= 0
            for i in range(len(value)):
                if value[i] >=4:
                    
                    count += 1        
            freshness= count/len(value)      #Finding freshness         

            print(freshness)
    else:
        
        print("\nFor 1D List: ", list_of_num)
        count= 0
        for i in range(len(list_of_num)):
            if list_of_num[i] >=4:
                count += 1
        freshness= count/len(list_of_num)  #Finding freshness   
        print(freshness)

#=========== For Dictionary Function  defination ======================================
def dict_fresh(my_dict):
    print("\nFor Dictionary: ", my_dict)
    for key, value in my_dict.items():
        count= 0
        for i in range(len(value)):
            if value[i] >=4:
                count += 1
        freshness= count/len(value)    #Finding freshness   
        if (freshness> 0.7):
            print(key)

            
movies = {'ET': [5,5,5,2], 'The Room':[1,1,1], 'Forrest Gump':[5,4,3]}
dict_fresh(movies)  #Function call

##fresh([2,4,1,5,4])   #Function call
##fresh([[5,5,5,2], [1,1,1], [5,4,3]])   #Function call
##
##dict_fresh({'ET': [5,5,5,2], 'The Room':[1,1,1], 'Forrest Gump':[5,4,3]})  #Function call


