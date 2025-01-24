# dash
import dash
from dash import html,dcc

import feffery_antd_components as fac
import feffery_leaflet_components as flc
from feffery_dash_utils.style_utils import style

from dash.dependencies import Input, Output
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
                            dbc.Input(placeholder="Enter Your age",type="number",required=True),
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
                            dbc.InputGroupText("评估你的水平"),
                            dbc.Input(placeholder="Your Score",type="number",required=True),
                            dbc.Button("确认", color="light",type="submit"),
                        ],
                        
                    ),
                    dbc.FormText(
                        "参考数据来源：YMCA of the USA, 2000",
                        color="secondary",
                    ),
                    ]
                )
                ],
            ),
            ],
            justify="center",
        ),
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


