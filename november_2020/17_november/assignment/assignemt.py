f = open('assignments.txt', 'r')

for line in f:

  grades = line.rstrip()

  marks = grades.split(',')

  total = 0.0

  for g in marks:

    total = total + int(g)

  print (f"For Student having {line} \ntotal sum is: ",total)

f.close()
