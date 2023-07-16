import pandas as pd
import plotly.express as px

df = pd.read_csv('C:/signin/hari/python/dataset/d1.csv') # Use forward slashes for file path

fig = px.line(df, x='PredictionDate', y='PredictedColumn', title='Predicted Sales over Time')
fig.show()
