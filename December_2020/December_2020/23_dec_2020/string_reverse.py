
def get_reverse_char(char):

  alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

  if len(char) > 1:

    return None

  char= char.upper()

  if char not in alpha:

    return None

  return reverse_alpha[alpha.index(char)]



def main():

#=============  Changes Made Here to convert the input string into Upper Case ===============================
  #input_string= (input('Input String:')).upper()  #Converted it into upper case
  input_string= (input('Input String:'))
  #print(input_string)
  output_string= ''

  for ch in input_string:

    ch= get_reverse_char(ch)

    if ch== None:

      output_string= None

      break

    output_string += ch

  print('Output String:', output_string)

#calling main function

main()
