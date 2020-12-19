increment = 0
mystr = input("Please enetr a color: ")
print(mystr)
increment =int(input("Please enter the increment: "))
counter=0
changes = 0

for ch in mystr:
    counter = counter + 1
    if counter == increment:
        newch = ch.upper()
        counter = 0
    else:
        newch =ch.lower()
    print(newch, end="")  #This is the changes made
    
    if ch != newch:        
        changes = changes + 1

print("\n\nThere were", changes, "changes")
