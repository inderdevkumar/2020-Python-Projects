
def read_tsv_file(tsv_file):
    import os
    output = []
    with open(tsv_file) as instream:
        for line in instream:
            line = line.strip(os.linesep)
            line_list = line.split(',')
            output.append(line_list)
    return(output)

def yes_or_no(message):
    answer = 'blah'
    while not answer in 'yn':
        answer = input(message)
        answer = answer.lower()
        if (len(answer) > 0) and (answer[0] in 'yn'):
            if answer[0] == 'y':
                return(True)
            elif answer[0] == 'n':
                return(False)
        else:
            print('Please answer "yes" or "no".')

def write_line_list_to_file(line_list,filename):
    
    with open(filename,'w') as outstream:
        for line in line_list:
            outstring = ''
            for item in line:
                outstring = outstring+item+'\t'
            outstring = outstring[:-1]+'\n'
            
            outstream.write(outstring)


#================  Changes made only in this function ============================================================
            
def find_shoe_swap_partner(shoe_file):
    ## see http://shoewap.com
    import os
    left_dictionary = {}
    right_dictionary = {}
    
    if os.path.isfile(shoe_file):
        line_list = read_tsv_file(shoe_file)
        
        for line in line_list:  # Code changed

            #==============  Below Logic Changed to make the problem simpler==============================
            splitted_list = line[0].split("\t")
            
            person= splitted_list[0]
            left_shoe= splitted_list[1]
            right_shoe= splitted_list[2]

            #===============================================
            
            if left_shoe != right_shoe:
                if left_shoe in left_dictionary:
                    left_dictionary[left_shoe].append(person)
                else:
                    left_dictionary[left_shoe] = [person]
                if right_shoe in right_dictionary:
                    right_dictionary[right_shoe].append(person)
                else:
                    right_dictionary[right_shoe] = [person]
    else:
        line_list = [['Name','Left','Right']]
    if yes_or_no('Would you like to participate in our shoe swap service?'):
        name = input('What is your name? ')
        left_size = input('What is the size of your left shoe? ')
        right_size = input('What is the size of your right shoe? ')
        ## round(number,1) rounds number to one decimal place
        if left_size == right_size:
            print('I am sorry, but you do not qualify for our service.')
            return(False) ## exit from program

        #==========================  Logic Changed   in elif ======================================
        elif (right_size in left_dictionary) and (left_size in right_dictionary):
            print("Left dict: ", left_dictionary)
            print("Left dict: ", right_dictionary)
            ## "in" tests for keys in dictionary
            for person in right_dictionary[left_size]:   #Swapped left_size  and right_size
                
                if person in left_dictionary[right_size]:   #Swapped left_size  and right_size
                    
                    print('Congratulations, we have found a shoe swap partner for you.')
                    print('Your shoe swap partner is', person+'!')
                    print('We will remove',person,'from our database.')
                    left_dictionary[right_size].remove(person)
                    right_dictionary[left_size].remove(person)
                    new_line_list = []

                    #===================  Logic Changed  =============================================
                    for index in range(len(line_list)):

                        new_splitted_list= line_list[index][0].split("\t")
                        person_to_check= new_splitted_list[0]
                        
                        if (person_to_check != person):
                            
                            new_line_list.append(line_list[index])

                    
                    write_line_list_to_file(new_line_list,shoe_file)     

                            
                    ## rewrite to file here
                    return(person)
        ## if a match was found, the return would exit the function
        ## Otherwise, we add person to the database.
        print('We currently do not have a shoe swap partner for you.')
        print('We are entering your name in our database')
        line_list.append([name,left_size,right_size])
        write_line_list_to_file(line_list,shoe_file)


# =================   Below all are newly added ==================================================
shoe_file  = r"F:\Python_Projects\course_hro_proects\python\December_2020\December_2020\19_dec_2020\tsv_file.tsv"  #Path of my tsv file
while True:
    find_shoe_swap_partner(shoe_file)  #Function call with parameter
