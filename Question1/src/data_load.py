import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/content/raw_data.csv')
df

#checking for the null values
df.isnull().sum()
