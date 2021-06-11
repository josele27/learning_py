import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


class PdReader:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def show_head(self):
        print(self.data.head())

    def get_total(self, start=None, end=None):
        start = start or 0
        end = len(self.data) if not end or end >= len(self.data) else end
        return sum(self.data.iloc[i]['Volume'] for i in range(start, end))