import re

def stringToList(string):
    parms = '\n'
    tags = '(<\s*\w+\s*' + parms + '\s*/?>)'
    return re.findall(r'[\w\.-]+@[\w\.-]+', string)

text= """ Consumer price Index:
           +0.2% in Sep 2020

           unemployment Rate:
           +7.9% in Sep 2020

           Producer Price Index:
           +0.4% in Sep 2020

           Employement Cost Index:
           +0.5% in 2nd Qtr of 2020 """

new_text= text.replace("in", "")
print(new_text)
print(stringToList(new_text))
