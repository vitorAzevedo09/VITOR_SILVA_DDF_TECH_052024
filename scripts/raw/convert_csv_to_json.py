#importing pandas as pd 
import pandas as pd 

df = pd.read_csv(r'../../data/online_retail_II.csv')
df.to_json (r'../../data/online_retail_II.json')
