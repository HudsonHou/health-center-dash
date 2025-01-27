# dash
import dash
from dash import html,dcc

import feffery_antd_components as fac
import feffery_leaflet_components as flc
from feffery_dash_utils.style_utils import style

from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import json

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
import sqlite3
def fetch_data():
    conn = sqlite3.connect('data/base.db')
    cursor = conn.cursor()
    
    # 获取列名
    cursor.execute('PRAGMA table_info(sit_and_reach);')
    columns = [description[1] for description in cursor.fetchall()]
    
    # 获取数据
    cursor.execute('SELECT * FROM sit_and_reach')
    data = cursor.fetchall()
    
    conn.close()
    
    # 使用列名和数据创建DataFrame
    return pd.DataFrame(data, columns=columns)

def render():
    
    return dbc.Container([
        dcc.Store(id='store-sit-reach',storage_type='local',data=fetch_data().to_json()),
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
                dcc.Loading(
                    children=[
                        dbc.Alert(
                        "请输入以上信息，开始评估你的体前屈水平吧~",
                        id="alert",
                        dismissable=False,
                        is_open=True,
                        color="info",
                        ),
                    ],
                    overlay_style={"visibility":"visible", "filter": "blur(2px)"},
                    # type="circle",
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
                dcc.Loading(
                    children=[dcc.Graph(id="fig-mele",config={'displayModeBar': False},className="glass-box",style={"height":300})],
                    overlay_style={"visibility":"visible", "filter": "blur(2px)"},
                    type="circle",
                    
                ),
                
                ],
                width="100%",
            ),
            ],
            justify="center",style={"marginBottom":10}
        ),
        # fac.AntdDivider(""),
        
        dbc.Row([
            dbc.Col([
                dcc.Loading(
                    children=[dcc.Graph(id="fig-female",config={'displayModeBar': False},className="glass-box",style={"height":300})],
                    overlay_style={"visibility":"visible", "filter": "blur(2px)"},
                    type="circle",
                ),
                ],
                width="100%",
            ),
            ],
            justify="center", style={"marginBottom":10} 
        ),
        
    ], fluid=True,style={"maxWidth": "430px"}
    )

# 更新dcc.Store中的数据

    
    
@app.callback(
    [Output("alert", "children"),
     Output("alert", "color"),
     ],
    Input("submit", "n_clicks"),
    [State("age", "value"), State("gender", "value"), State("score", "value"),State("store-sit-reach", "data")],
    prevent_initial_call=True
)
def find_ecdf(n_clicks,age, gender, value, data):
    if age and gender and value:
        
        df=pd.DataFrame(json.loads(data))

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

## 从store加载图像
@app.callback(
    [Output("fig-mele", "figure"),
     Output("fig-female", "figure"),],
    Input("store-sit-reach", "data")
)
def update_graph(data):
    # 检查data是否非空
    df = pd.DataFrame(json.loads(data))
    fig_mele = sit_reach_figs.render(df, "male")
    fig_female = sit_reach_figs.render(df, "female")
    return fig_mele, fig_female 
  

