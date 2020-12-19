names = ["Euclid", "Archimedes", "Newton", "Descartes", "Fermat", "Turing", "Euler", "Einstein",
          "Boole", "Fibonacci", "Lovelace", "Noether", "Nash", "Wiles", "Cantor", "Gauss", "Plato"] 

len_names= len(names)
total_length= 0
for element in names:
    len_each_elemet= len(element)
    total_length= total_length + len_each_elemet

average= total_length/len_names

def alphacounts():
    
print(f"{average} is the average length of all entries in the list names")
