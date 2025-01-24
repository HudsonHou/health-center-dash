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
        ),
        xaxis=dict(
            # tickprefix="°",##前缀
            title=None,## 标题
            ticksuffix="in",##后缀
            showgrid=True,
            gridcolor='rgb(204, 204, 204)',
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
        ),
        yaxis_range=[0, 100],
        xaxis_range=[3, 25],
        legend=dict(
            title="年龄组",
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.1
        ),
        margin={'l': 0, 'b': 0, 'r': 0, 't': 40, 'pad': 0},
        template="plotly_white",
        
        
        # hovermode='x unified',
        # template='plotly_white'
    )
def render(gender:str):
    # 创建一个DataFrame，包含不同年龄段和性别的数据
    data=pd.DataFrame(
        data=[
            [22, 24, 21, 23, 21, 22, 19, 21, 17, 20, 17, 20],
            [20, 22, 19, 21, 19, 21, 17, 20, 15, 19, 15, 18],
            [19, 21, 17, 20, 17, 19, 15, 18, 13, 17, 13, 17],
            [18, 20, 17, 20, 16, 18, 14, 17, 13, 16, 12, 17],
            [17, 19, 15, 19, 15, 17, 13, 16, 11, 15, 10, 15],
            [15, 18, 14, 17, 13, 16, 11, 14,  9, 14,  9, 14],
            [14, 17, 13, 16, 13, 15, 10, 14,  9, 13,  8, 13],
            [13, 16, 11, 15, 11, 14,  9, 12,  7, 11,  7, 11],
            [11, 14,  9, 13,  7, 12,  6, 10,  5,  9,  4,  9]
        ],
        index=[90,80,70,60,50,40,30,20,10],
        columns=["m_18-25","wm_18-25","m_26-35","wm_26-35","m_36-45","wm_36-45","m_46-55","wm_46-55","m_56-65","wm_56-65","m_over65","wm_over65"]
    )
    data.sort_index(inplace=True)

    # 重置索引并将数据转换为长格式
    data_long = data.reset_index().melt(id_vars='index', var_name='category', value_name='value')

    # 提取性别（首字母'm'为男性，'w'为女性）
    data_long['gender'] = data_long['category'].str[0].map({'m': 'male', 'w': 'female'})

    # 提取年龄段
    data_long['age_group'] = data_long['category'].str.split('_').str[1]

    # 可选：删除原category列并重新排列列顺序
    data_long = data_long[['index', 'gender', 'age_group', 'value']]

    # data_long
    
    fig = px.line(
        data_long[data_long['gender'] == gender],
        x="value",
        y="index",
        # color="gender",
        # title=titel,
        color="age_group",
        markers=True,
        # height=800,
        color_discrete_sequence=px.colors.qualitative.G10,

    )
    update_figure(fig)
    
    
    
    return fig




