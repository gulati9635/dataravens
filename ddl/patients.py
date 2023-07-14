import pandas as pd

import json
data = json.load(open('..\sample.json'))

df = pd.DataFrame(data["patients"])

print(df.columns)

print(df.to_string(index=False))