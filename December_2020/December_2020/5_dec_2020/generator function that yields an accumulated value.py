def genAccum_with_yield(seq, fn):
    '''
        >>> add = lambda x, y: x + y
        >>> mul = lambda x, y: x * y
        >>> list(genAccum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], add))
        [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        >>> list(genAccum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], mul))
        [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    '''
    iteration=iter(seq)
    element=next(iteration)
    
    yield element
    for i in iteration:
        element=fn(element, i)   
        yield element

def genAccum_without_yield(seq, fn):
    '''
        >>> add = lambda x, y: x + y
        >>> mul = lambda x, y: x * y
        >>> list(genAccum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], add))
        [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        >>> list(genAccum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], mul))
        [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    '''
    iteration= iter(seq)
    element= next(iteration)
    new_list_num = []
    
    for i in iteration:
        element=fn(element, i)   
        print(element)
        
add = lambda x, y: x + y    
output= list(genAccum_with_yield([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], add))
for num in output:
    list_num = []
    list_num.append(num)
    
    print (list_num)

(genAccum_without_yield([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], add))
