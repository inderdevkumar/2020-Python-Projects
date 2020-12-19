def main():
    choice= 1

    while choice:
        
        operation_input= input("Ënter Operation: ")

        if (operation_input == "|" or operation_input == "&"  or operation_input == "^"  or operation_input == "q" ):
            choice= 0
            number_of_operand= int(input("Enter number of operands: "))
            list_of_operand= []
            for i in range(1, number_of_operand+1):

                choice1= 1
                
                while choice1:
                    
                    
                    operand_input= input(f"Enter Operand {i}: ")
                    if (len(operand_input)< 9):
                        choice1= 0
                        length_of_operand= len(operand_input)
                        if (length_of_operand == 0):
                            operand_input= "00000000" + operand_input
                            list_of_operand.append(operand_input)
                            
                            
                        elif (length_of_operand == 1):
                            operand_input= "0000000" + operand_input
                            list_of_operand.append(operand_input)
                            

                        elif (length_of_operand == 2):
                            operand_input= "000000" + operand_input
                            list_of_operand.append(operand_input)
                            

                        elif (length_of_operand == 3):
                            operand_input= "00000" + operand_input
                            list_of_operand.append(operand_input)
                            
                            
                        elif (length_of_operand == 4):
                            operand_input= "0000" + operand_input
                            list_of_operand.append(operand_input)
                            
                            
                        elif (length_of_operand == 5):
                            operand_input= "000" + operand_input
                            list_of_operand.append(operand_input)
                            
                            
                        elif (length_of_operand == 6):
                            operand_input= "00" + operand_input
                            list_of_operand.append(operand_input)
                            
                            
                        elif (length_of_operand == 7):
                            operand_input= "0" + operand_input
                            list_of_operand.append(operand_input)
                            
                            
                        else:
                            operand_input=  operand_input
                            list_of_operand.append(operand_input)
                            
                            
                        
                    else:
                        print("Please enter an 8-digit hexadecimal integer")
                        continue
                           
            hex_binary(list_of_operand, operation_input)
        else:
            print("Please enter |, &, ^, or q")
            continue

def check_hex(value):
    pass
def hex_opeartion(values, operation):
    pass

def hex_binary(values, operation):
    print(values)

    hex_value_with_operation= ""
    binary_value_with_opeartion= ""
    print("Binary Operation: \n")
    for i in range(len(values)):

        hex_value_with_operation= hex_value_with_operation + value +operation
       
        # Code to convert hex to binary 
        res = "{0:08b}".format(int(value, 16))
        
        binary_value_with_opeartion= binary_value_with_opeartion + res + " " + operation
    new_hex_value_with_operation= hex_value_with_operation[:-1]
    binary_value_with_opeartion=  binary_value_with_opeartion[:-1]
    
    print(hex_value_with_operation)
    print(binary_value_with_opeartion)

main()
