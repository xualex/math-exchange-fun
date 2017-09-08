import json
import requests
import pandas as pd

file_name = 'https://api.stackexchange.com/2.2/answers?fromdate=1504656000&todate=1504742400&order=desc&sort=activity&site=stackoverflow'
#Get JSON file
file_data = requests.get(file_name)
my_data = json.loads(file_data.text)
df = pd.DataFrame(my_data)

print(df)
