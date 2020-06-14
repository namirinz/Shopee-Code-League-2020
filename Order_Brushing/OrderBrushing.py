import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('datasets/order_brush_order.csv')

df.loc[df['shopid'] == 93950878, 'userid'] = 512

print(df)

#print(df.head())
