num =  int(input("Enter total number(n): "))
chosen_num= int(input("Enter the number of item chosen(r): "))

# As we know, nPr= n!/(n-r)!

try:
    def npr(n, r):  #To find nPr= n!/(n-r)!
        n_factorial= 1
        diff= n-r
        diff_factorial= 1

        if r > n or n < 0 or r < 0:
            raise ValueError

        else:
            for count_n in range(1, n+1):       
                n_factorial= n_factorial* count_n

            for count_diff in range(1, diff+1):
                diff_factorial= diff_factorial * count_diff

            nPr= n_factorial/diff_factorial
            return nPr

    print("nPr is: ", npr(num, chosen_num))
    
except ValueError:
    
    print("ValueError Exception!")

 


