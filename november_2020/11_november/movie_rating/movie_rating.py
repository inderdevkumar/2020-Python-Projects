import os
import glob

user_ratings = []

def oscar_opinions(filename):
    file = open(filename, 'r')
    
    for line in file:
        line = line.strip().split('\t')
        user_ratings.append(line)
        print(user_ratings)

#os.path.isfile
                   
filename = 'movie_rating.tsv'

#oscar_opinions(filename)

files = glob.glob('*.tsv')
print(files)
for file in files:
    if(os.path.isfile(file)):
        oscar_opinions(filename)
    else:
        print("ERROR: FILE NOT FOUND")


for i in range(1, len(user_ratings)):
    user_ratings[i] = list(map(int, user_ratings[i]))


while True:
    print("Add one more user?")
    choice = input(" 'yes' or 'no' ").lower()
    if choice.lower()=='no':
        break
    else:
        number = len(user_ratings)
        new_user_list = []
        new_user_list.append(number)
        file = open(filename, 'a')
        for i in range(1, len(user_ratings[0])):
            print(user_ratings[0][i])
            print('Did you see the movie '+user_ratings[0][i]+'?')
            print('Enter a number from 0 to 5.')
            print('0 means you did not see the movie')
            print('Otherwise the ratings are: 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic')
            rating=int(input('What is your rating?'))
            new_user_list.append(rating)
            
        
        file.write("\n")
        file.write(" ".join(str(new_user_list)))

        file.close()
        
for i in range(1,len(user_ratings[0])):
    saw_move = 0
    total = 0
    for j in range(1, len(user_ratings)):
        if user_ratings[j][i]>0:
            total=total+user_ratings[j][i]
            saw_movie=saw_movie+1
            avg=round(total/saw_movie,2)
        if saw_movie == 0:
            print('Nobody saw',user_ratings[0][i])
        else:
            print('The movie',user_ratings[0][i],'had an average score of',avg,'.',saw_movie,'people saw it in our sample.')



