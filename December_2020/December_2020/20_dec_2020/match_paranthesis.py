#s= 'A (B) C'
s= 'A B) (C'
first_open_parens = s.find('(')
print(first_open_parens)
first_close_parens = s.find(')')
print(first_close_parens)
