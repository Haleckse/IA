import pandas as pd
import numpy as np
import matplotlib . pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv('bebe.csv')
df.drop('X', axis=1, inplace=True)

print(df.describe()) 

sns.pairplot(df)
