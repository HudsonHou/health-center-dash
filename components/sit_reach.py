# dash
import dash
from dash import html,dcc

import feffery_antd_components as fac
import feffery_leaflet_components as flc
from feffery_dash_utils.style_utils import style

from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

# 配置
from server import app
from config import MapConfig

# 地图组件
from maps.legend import Legend
from maps.basemap import Basemap
from maps import tile_selector, symbol_style
import dash_bootstrap_components as dbc
import feffery_antd_charts as fact

# 数据
from models.gpd_data import cbsdata, arcgisdata
import random

# figs
from figs import home,weight,sit_reach_figs
from datetime import date


def render():
    
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Form([
                    dbc.InputGroup(
                        [
                            dbc.InputGroupText("你的年龄"),
                            dbc.Input(placeholder="Enter Your age",type="number",required=True,id="age"),
                            # dbc.Button("确认", color="light"),
                        ],
                    
                    ),
                    dbc.InputGroup(
                        [
                            dbc.InputGroupText("你的性别"),
                            dbc.Select(
                                id="gender",
                                options=[
                                    {"label": "男性", "value": "male"},
                                    {"label": "女性", "value": "female"},
                                ],
                                # value="male",
                                required=True,
                                
                            ),
                            # dbc.Button("确认", color="light"),
                        ],
                    
                    ),
                    dbc.InputGroup(
                        [
                            dbc.InputGroupText("你的分数"),
                            dbc.Input(placeholder="Your Score",type="number",required=True, id="score"),
                            dbc.Button("确认", color="light",type="submit",id="submit"),
                        ],
                        
                    ),
                    # dbc.FormText(
                    #     "参考数据来源：YMCA of the USA, 2000",
                    #     color="secondary",
                    # ),
                    ]
                )
                ],
            ),
            ],
            justify="center",
        ),
        dbc.Row([
            dbc.Col([
                dbc.Alert(
                    "请输入以上信息，开始评估你的体前屈水平吧~",
                    id="alert",
                    dismissable=False,
                    is_open=True,
                    color="info",
                ),
                ],
                width="100%",
            ),
            ],
            justify="center", style={"marginBottom":10} 
        ),
        html.Div([
            html.P("数据来源：YMCA of the USA, 2000", 
                style={'fontSize': 12, 'color': 'gray'})
        ], style={'textAlign': 'center', 'marginTop': 20}),
        dbc.Row([
            dbc.Col([
                dcc.Graph(figure=sit_reach_figs.render(gender="male"),config={'displayModeBar': False},className="glass-box"),
                ],
                width="100%",
            ),
            ],
            justify="center",style={"marginBottom":10}
        ),
        # fac.AntdDivider(""),
        
        dbc.Row([
            dbc.Col([
                dcc.Graph(figure=sit_reach_figs.render(gender="female"),config={'displayModeBar': False},className="glass-box"),
                ],
                width="100%",
            ),
            ],
            justify="center", style={"marginBottom":10} 
        ),
        
    ], fluid=True,style={"maxWidth": "430px"}
    )
    
@app.callback(
    [Output("alert", "children"),
     Output("alert", "color"),
     ],
    Input("submit", "n_clicks"),
    [State("age", "value"), State("gender", "value"), State("score", "value")],
    prevent_initial_call=True
)
def find_ecdf(n_clicks,age, gender, value):
    if age and gender and value:
       
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
        data_long=data_long.rename(columns={"index":"ecdf"})
        df=data_long
        # 获取年龄分组,未满18按照18岁算
        def get_age_group(age):
            if age >= 66:
                return 'over65'
            elif 56 <= age <= 65:
                return '56-65'
            elif 46 <= age <= 55:
                return '46-55'
            elif 36 <= age <= 45:
                return '36-45'
            elif 26 <= age <= 35:
                return '26-35'
            elif age <= 25:
                return '18-25'
            
        age_group = get_age_group(age)

        # 筛选符合条件的行
        filtered_df = df[(df['gender'] == gender) & 
                        (df['age_group'] == age_group) & 
                        (df['value'] <= value)]
        
        if filtered_df.empty:
            ecdf=10
            return f"你的体前屈水平低于{ecdf}%的同龄人！", "danger"
            
        else:
            ecdf=filtered_df['ecdf'].max()
            return f"你的体前屈水平高于{ecdf}%的同龄人！", "success"
    else:
        return dash.no_update,dash.no_update
    # return ecdf
    # return render()


