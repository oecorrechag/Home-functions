import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots

data = {'year': [2010, 2011, 2012, 2013, 2014, 2015, 2016],
        'sales': [200, 400, 600, 800, 1000, 1200, 1400],
        'profit': [20, 50, 55, 88, 110, 150, 160]}
df = pd.DataFrame(data)

subfig = make_subplots(specs=[[{"secondary_y": True}]])

fig = px.line(df, x="year", y="sales")
fig2 = px.line(df, x="year", y="profit")

fig2.update_traces(yaxis="y2")

subfig.add_traces(fig.data + fig2.data)
subfig.layout.xaxis.title="Year"
subfig.layout.yaxis.title="Sales"
# subfig.layout.yaxis2.type="log"
subfig.layout.yaxis2.title="Profit"

subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
subfig.show()
