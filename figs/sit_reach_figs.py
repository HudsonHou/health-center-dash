import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go


def update_figure(fig:px.line):
    fig.update_layout(
        # title="坐位体前屈评估成绩 (YMCA)",
        yaxis=dict(
            # tickprefix="°",##前缀
            title=None,## 标题
            ticksuffix="%",##后缀
            showgrid=True,
            gridcolor='rgb(204, 204, 204)',
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            fixedrange=True
        ),
        xaxis=dict(
            # tickprefix="°",##前缀
            title=None,## 标题
            ticksuffix="in",##后缀
            showgrid=True,
            gridcolor='rgb(204, 204, 204)',
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            fixedrange=True
        ),
        yaxis_range=[0, 100],
        xaxis_range=[3, 25],
        legend=dict(
            title="年龄组",
            yanchor="top",
            y=1.3,
            xanchor="left",
            x=0,
            orientation="h",
        ),
        margin={'l': 0, 'b': 0, 'r': 0, 't': 40, 'pad': 0},
        template="plotly_white",
        dragmode=False,
    )
    fig.update_traces(hovertemplate= 
        '<b>Score</b>: %{x}<br>'+
        '<b>ECDF</b>: %{y}'
    )
def render(data,gender:str):
    df=pd.DataFrame(data)
    

    # data_long
    
    fig = px.line(
        df[df['gender'] == gender],
        x="value",
        y="ecdf",
        # color="gender",
        # title=titel,
        color="age_group",
        markers=True,
        height=300,
        color_discrete_sequence=px.colors.qualitative.G10,
        

    )
    update_figure(fig)
    
    
    
    return fig




