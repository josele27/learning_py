import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
PG = pd.read_csv('PG_1995-03_23_2017.csv', index_col = 'Date')
print(PG.head())
