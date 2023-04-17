import plotly.express as px
import plotly.subplots as sp

def conjuntoheats(fig1,fig2,fig3,fig4,t1,t2,t3,t4,savename):
    
    'Esta funcion recibe 4 figuras y 4 titulos y los une en una malla'
    
    figure1_traces = []
    figure2_traces = []
    figure3_traces = []
    figure4_traces = []

    for trace in range(len(fig1["data"])):
        figure1_traces.append(fig1["data"][trace])
    for trace in range(len(fig2["data"])):
        figure2_traces.append(fig2["data"][trace])
    for trace in range(len(fig3["data"])):
        figure3_traces.append(fig3["data"][trace])
    for trace in range(len(fig4["data"])):
        figure4_traces.append(fig4["data"][trace])

    fig = sp.make_subplots(rows=2, cols=2, subplot_titles=(t1,t2,t3,t4)) 

    # Get the Express fig broken down as traces and add the traces to the proper plot within in the subplot
    for traces in figure1_traces:
        fig.append_trace(traces, row=1, col=1)
    for traces in figure2_traces:
        fig.append_trace(traces, row=1, col=2)
    for traces in figure3_traces:
        fig.append_trace(traces, row=2, col=1)
    for traces in figure4_traces:
        fig.append_trace(traces, row=2, col=2)

    fig.update_layout(coloraxis=dict(colorscale='RdBu_r'), showlegend=False)
    fig.update_yaxes(autorange="reversed")
    fig.update_xaxes(
        tickvals=[1,5,9,13,18,22,26,31,35,39,44,48],
        ticktext=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    )
    fig.update_yaxes(
        tickvals=[12,13,14,15,16,17,18,19,20,21,22],
        ticktext=[12,13,14,15,16,17,18,19,20,21,22])
    fig.update_layout(title='Minutos estancia promedio por hora vs semana')
    fig.update_xaxes(tickangle=300)

    return fig