import itertools
x = "ab"
all_ghjkl= [''.join(p) for p in itertools.product(x, repeat=2)]
print(all_ghjkl)

or

from itertools import product
for roll in product(x, repeat = 2):
    
    print(*roll)
