# import some stuff
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# create some data
df = pd.DataFrame()
n = 50
df["Time"] = np.arange(n)
df["Linear-"] = np.arange(n)+np.random.rand(n)
df["Linear+"] = np.arange(n)+np.random.rand(n)
df["Log-"] = np.arange(n)+np.random.rand(n)
df["Log+"] = np.arange(n)+np.random.rand(n)
df.set_index("Time", inplace=True)


subfig = make_subplots(specs=[[{"secondary_y": True}]])

# create two independent figures with px.line each containing data from multiple columns
fig = px.line(df, y=df.filter(regex="Linear").columns, render_mode="webgl",)
fig2 = px.line(df, y=df.filter(regex="Log").columns, render_mode="webgl",)

fig2.update_traces(yaxis="y2")

subfig.add_traces(fig.data + fig2.data)
subfig.layout.xaxis.title="Time"
subfig.layout.yaxis.title="Linear Y"
subfig.layout.yaxis2.type="log"
subfig.layout.yaxis2.title="Log Y"

subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
subfig.show()
