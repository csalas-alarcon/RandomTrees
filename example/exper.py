import numpy as np
import pandas as pd
from collections import deque

# generate some data
# define features and target values
data = {
    'wind_direction': ['N', 'S', 'E', 'W'],
    'tide': ['Low', 'High'],
    'swell_forecasting': ['small', 'medium', 'large'],
    'good_waves': ['Yes', 'No']
}

# create an empty dataframe
data_df = pd.DataFrame(columns=data.keys())
print(f"data_df: {data_df}")

np.random.seed(42)
# randomnly create 1000 instances
for i in range(1000):
    data_df.loc[i, 'wind_direction'] = str(np.random.choice(data['wind_direction'], 1)[0])
    data_df.loc[i, 'tide'] = str(np.random.choice(data['tide'], 1)[0])
    data_df.loc[i, 'swell_forecasting'] = str(np.random.choice(data['swell_forecasting'], 1)[0])
    data_df.loc[i, 'good_waves'] = str(np.random.choice(data['good_waves'], 1)[0])

print("RELLENITO")
print(data_df)

data_df.head()
print('La HEAD')
print(data_df.head())

# separate target from predictors
X = np.array(data_df.drop('good_waves', axis=1).copy())
y = np.array(data_df['good_waves'].copy())
feature_names = list(data_df.keys())[:3]

print(X)
print(y)
print(feature_names)

print(np.array(data_df.drop(feature_names, axis=1)))