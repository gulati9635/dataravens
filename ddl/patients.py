import  pandas as pd
from Tools.scripts.dutree import display

df = pd.read_json("..\data.json")
display(df)