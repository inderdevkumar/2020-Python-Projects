import os
import re

# Enter your code here 
sample_text= ['199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245',

 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985',

 '199.120.110.21 - - [01/Jul/1995:00:00:09 -0400] "GET /shuttle/missions/sts-73/mission-sts-73.html HTTP/1.0" 200 4085',

 'burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0',

 '199.120.110.21 - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/missions/sts-73/sts-73-patch-small.gif HTTP/1.0" 200 4179',

 'burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0',

 'burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.gif HTTP/1.0" 200 0',

 '205.212.115.106 - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/countdown.html HTTP/1.0" 200 3985',

 'd104.aa.net - - [01/Jul/1995:00:00:13 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985',

 '129.94.144.152 - - [01/Jul/1995:00:00:13 -0400] "GET / HTTP/1.0" 200 7074',

 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310',

 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786',

 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204',

 'd104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310',

 'd104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786']

def func1():
    list_of_values= []
    for sample_text1 in sample_text:
        
        spltAr = sample_text1.split("://")  #Taken help of your dempo code, Its used to amke list
        list_of_values.append(spltAr[0].split("?")[0].split(' - - ')[0].split(':')[0].lower())  #appending all 0 index value of list
    print(list_of_values)


def func2():
    list_of_values= []
    
    for sample_text1 in sample_text:
        list_of_values.append(sample_text1[sample_text1.find("^[ ]$")+1:].split())#Regex used to get all words between "[" and "]". Than appending
        

    flat_list1 = [sublist[3].replace("[", "") for sublist in list_of_values] #Getting the required index value as a list from list using list comprehension
    flat_list2 = [sublist[4].replace("]", "") for sublist in list_of_values]  #Getting the required index value as a list from list using list comprehension

    res = [i +" "+ j for i, j in zip(flat_list1, flat_list2)]  #Adding two lists with with the required index
    print(res)
    

def func3():
    list_of_values= []
    
    for sample_text1 in sample_text:
        list_of_values.append(sample_text1[sample_text1.find("^[ ]$")+1:].split())  #Regex used to get all words between "[" and "]". Than appending
        

    flat_list1 = [sublist[5].replace('"', "") for sublist in list_of_values]   #Getting the required index value as a list from list using list comprehension
    flat_list2 = [sublist[6] for sublist in list_of_values]   #Getting the required index value as a list from list using list comprehension
    flat_list3 = [sublist[7].replace('"', "") for sublist in list_of_values]    #Getting the required index value as a list from list using list comprehension
    
    merged_list = [(flat_list1[m], flat_list2[m], flat_list3[m]) for m in range(0, len(flat_list2))] #Merging lists into tuple
    print(merged_list)
    
def func4():
    list_of_values= []
    
    for sample_text1 in sample_text:
        list_of_values.append(sample_text1[sample_text1.find("^[ ]$")+1:].split()) #Regex used to get all words between "[" and "]". Than appending
        

    flat_list1 = [sublist[8] for sublist in list_of_values]#Getting the required index value as a list from list using list comprehension
    
    print(flat_list1)

def func5():
    list_of_values= []
    
    for sample_text1 in sample_text:
        list_of_values.append(sample_text1[sample_text1.find("^[ ]$")+1:].split())
        

    flat_list1 = [sublist[9] for sublist in list_of_values]   #Getting the required index value as a list from list using list comprehension

    
    print(flat_list1)
  

if __name__ == "__main__":
    print("Start")
    print("#############  Function1 Output: ####################\n\n")
    func1()
    print("#############  Function2 Output: ####################\n\n")
    func2()
    print("#############  Function3 Output: ####################\n\n")
    func3()
    print("#############  Function4 Output: ####################\n\n")
    func4()
    print("#############  Function5 Output: ####################\n\n")
    func5()
