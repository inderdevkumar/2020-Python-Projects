import pandas as pd
import matplotlib.pyplot as plt


weather_data = [('1/1/2020', '20', 'rain'),

        ('1/2/2020', '25', 'sunny'),

        ('1/3/2020', '20', 'snow'),

        ('1/4/2020', '24', 'snow'),

        ('1/5/2020', '32', 'rain'),

        ('1/6/2020', '33', 'sunny'),

        ('1/7/2020', '26', 'rain')]



df = pd.DataFrame(weather_data, columns=['day', 'temperature', 'event'])
print(df)
