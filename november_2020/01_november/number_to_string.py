#Number converter till 100 is

##num1_19 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
##            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
##            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
##            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
##
##for_2_digits = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
##
##num_in_tenth_series = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
##
##
###100000000
##def InWords(Number):
##    
##    if 0 <= Number <= 19:
##        return num1_19[Number]
##    elif 20 <= Number <= 99:
##        tens, remainder = divmod(Number, 10)
##        return for_2_digits[tens - 2] + ' ' + num1_19[remainder] if remainder else for_2_digits[tens - 2]
##    else:
##        return 'Number out of range.'

##user_input= int(input("Enter your number: "))
##print(f"Numbers in words for {user_input} is: {InWords(user_input)}")




#Number converter for any input numbers
print("Number To Words Converter:\n\n") 
number=int(input("Enter Number: ")) 
word=str(number) 
print("\n")

def InWords(number): 
    w={0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"} 
    f={2:"Twen",3:"Thir",4:"For",5:"Fif",6:"Six",7:"Seven",8:"Eigh",9:"Nine"} 
    t={11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"} 
    if len(number)==1:
        return(w[int(number)]) 
    elif len(number)==2 and number[0]=="0" and number[1]=="0":
        return("") 
    elif len(number)==2 and number[0]=="0":
        return (w[int(number[1])]) 
    elif len(number)==2: 
        if int(number) in range(11,20):
            return(t[int(number)]) 
        elif int(number[1])==0: 
            if int(number)==10:
                return("Ten") 
            else:
                return(f[int(number[0])]+"ty") 
        else:
            return(f[int(number[0])]+"ty"+" "+w[int(number[1])]) 
def hun_num(x): 
    w1={0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"} 
    if len(x)==3 and x[0]!="0" and x[1]=="0" and x[2]=="0": 
        return(w1[int(x[0])]+" "+"Hundred") 
    elif len(x)==3 and x[0]!="0": 
        a1=(x[1]+x[2]) 
        return(w1[int(x[0])]+" "+"Hundred "+"and "+InWords(a1)) 
    elif len(x)==3 and x[0]=="0":
        return(InWords(x[1]+x[2])+" ") 
    else:
        return(InWords(x)) 
def seg3(s): 
    out = [] 
    while len(s): 
        out.insert(0, s[-3:]) 
        s = s[:-3] 
    return out

def q(x): 
    if x=="000":
        return(0) 
    elif x=="00":
        return(0) 
    elif x=="0":
        return(0) 
    else:
        return(1)
    
v=seg3(word) 
aa={0:"",1:"Thousand",2:"Million",3:"Billion",4:"Trillion",5:"Quadrillion",6:"Quintillion",7:"Hextillion",8:"Septillion",9:"Octillion",10:"Nonillion",11:"Decillion",12:"Undecillion",13:"Duodecillion",15:"Quattuordecillion",16:"Quindecillion",17:"Hexdecillion",18:"Septdecillion",19:"Octodecillion",20:"Novemdecillion",21:"Vigintillion",14:"Tredecillion",22:"Unvigintillion",23:"Duovigintillion",24:"Trevigintillion",25:"Quattuorvigintillion",26:"Quinvigintillion",27:"Hexvigintillion",28:"Septvigintillion",29:"Octovigintillion",30:"Novemvigintillion",31:"Trigintillion",32:"Untrigintillion",33:"Duotrigintillion"} 

if int(word)==0:
    s="Zero" 
else: 
    s1="" 
    for i in range(len(v)):
        s1= s1+(hun_num(v[i]))+(" "+aa[len(v)-1-i]+", ")*q(v[i]) 
    s=s1[:len(s1)-3] 
print(f"In word, number for {number} is: -> {s}.") 
