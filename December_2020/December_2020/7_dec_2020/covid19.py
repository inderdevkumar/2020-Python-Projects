import datetime
import numpy as np
import matplotlib.pyplot as plt


# open input file
f = open("covid-19_data.txt", "r")


# lists for dates and positive cases
dates = []
pos = []


# read all lines
for line in f:
    words = line.split(" ")
    dates.append(datetime.datetime.strptime(words[0], '%Y-%m-%d').date())
    pos.append(int(words[2]))
    print(dates)

pos = np.cumsum(pos)


# plot bar graph
plt.bar(dates, pos)
# plot title and axes lables
plt.title('Positive COVID-19 Cases in Indiana')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.xticks(np.arange(dates[4], dates[-1], datetime.timedelta(days=7)), rotation=30)
# yaxis ticks start from 0 to end with steps of 1000
plt.yticks(np.arange(0, pos[-1], 1000))
plt.savefig("covid-19_cases.pdf")
plt.show()
