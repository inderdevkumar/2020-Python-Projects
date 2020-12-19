def fcn(n ,s):
    if (n<1):
        print("done", s)
    else:
        print("here", s*n)
        print("call with : ", n-2, s)
        fcn(n-2, s)
        print("after all")

string = "name"
x= 7
print("begin")
fcn(x, string)
print("end")
