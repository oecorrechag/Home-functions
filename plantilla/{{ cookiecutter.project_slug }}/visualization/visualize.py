import re
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px

def scatter_plot_x(data: pd.DataFrame, x, y):
    fig = px.scatter(data, x=x, y=y)
    return fig